"""Utility functions for the entire package.

"""
from typing import Tuple

from astropy import units
import numpy as np
import numpy.typing as npt


def nanoTesla2Gauss(nT_values: npt.ArrayLike) -> npt.NDArray:
    """Convert array in nano tesla to Gauss.

    Args
      nT_values: nano tesla values
    Returns
      gauss_values: array of gauss values, same shape
    """
    # ignore types because astropy units broken with typing
    with_units = np.array(nT_values) * units.nT  # type: ignore
    as_gauss = with_units.to(units.G).value

    return as_gauss


def sp2cart_point(r: float, phi: float, theta: float) -> Tuple[float, float, float]:
    """Spherical coordinate to cartesian coordinate conversion for a single point.

    Args
      r: radius
      phi: longitude
      theta: latitude
    Returns
      x, y, z: Cartesian coordinates
    """
    point = sp2cart(r=r, phi=phi, theta=theta)  # returns tuple of 0d arrays
    point = tuple(np.array(point).tolist())

    return point


def cart2sp_point(x: float, y: float, z: float) -> Tuple[float, float, float]:
    """Spherical coordinate to cartesian coordinate conversion for a single point.

    Args
      x, y, z: Cartesian coordinates
    Returns
      r: radius
      phi: longitude
      theta: latitude
    """
    point = cart2sp(x=x, y=y, z=z)  # returns tuple of 0d arrays
    point = tuple(np.array(point).tolist())

    return point


# Function forked from https://bitbucket.org/isavnin/ai.cs/src/master/src/ai/cs.py
# because broken in Python 3.12
def cart2sp(x, y, z):
    """Converts data from cartesian coordinates into spherical.

    Args:
        x (scalar or array_like): X-component of data.
        y (scalar or array_like): Y-component of data.
        z (scalar or array_like): Z-component of data.

    Returns:
        Tuple (r, theta, phi) of data in spherical coordinates.
    """
    x = np.asarray(x)
    y = np.asarray(y)
    z = np.asarray(z)
    scalar_input = False
    if x.ndim == 0 and y.ndim == 0 and z.ndim == 0:
        x = x[None]
        y = y[None]
        z = z[None]
        scalar_input = True
    r = np.sqrt(x**2+y**2+z**2)
    theta = np.arcsin(z/r)
    phi = np.arctan2(y, x)
    if scalar_input:
        return (r.squeeze(), theta.squeeze(), phi.squeeze())
    return (r, theta, phi)


# Function forked from https://bitbucket.org/isavnin/ai.cs/src/master/src/ai/cs.py
# because broken in Python 3.12
def sp2cart(r, theta, phi):
    """Converts data in spherical coordinates into cartesian.

    Args:
        r (scalar or array_like): R-component of data.
        theta (scalar or array_like): Theta-component of data.
        phi (scalar or array_like): Phi-component of data.

    Returns:
        Tuple (x, y, z) of data in cartesian coordinates.
    """
    r = np.asarray(r)
    theta = np.asarray(theta)
    phi = np.asarray(phi)
    scalar_input = False
    if r.ndim == 0 and theta.ndim == 0 and phi.ndim == 0:
        r = r[None]
        theta = theta[None]
        phi = phi[None]
        scalar_input = True
    x = r*np.cos(theta)*np.cos(phi)
    y = r*np.cos(theta)*np.sin(phi)
    z = r*np.sin(theta)
    if scalar_input:
        return (x.squeeze(), y.squeeze(), z.squeeze())
    return (x, y, z)


def lfm_get_eq_slice(data):
    """Gets an equitorial slice from data on an LFM grid.

    args
      data: numpy array, 3D on LFM grid
    Returns
      eq_c: numpy array, 2D equitorial slice only
    """
    # Adapted from PyLTR
    nk = data.shape[2] - 1
    dusk = data[:, :, 0]
    dawn = data[:, :, nk // 2]
    dawn = dawn[:, ::-1]
    eq = np.hstack((dusk, dawn[:, 1:]))
    eq_c = 0.25 * (eq[:-1, :-1] + eq[:-1, 1:] + eq[1:, :-1] + eq[1:, 1:])
    eq_c = np.append(eq_c.transpose(), [eq_c[:, 0]], axis=0).transpose()

    return eq_c


def lfm_get_mer_slice(data):
    """Gets an meridional slice from data on an LFM grid.

    args
      data: numpy array, 3D on LFM grid
    Returns
      mer_c: numpy array, 2D meridional slice only
    """
    # Adapted from pyLTR
    nk = data.shape[2] - 1
    north = data[:, :, nk // 4]
    south = data[:, :, 3 * nk // 4]
    south = south[:, ::-1]  # reverse the j-index
    mer = np.hstack((north, south[:, 1:]))
    mer_c = 0.25 * (mer[:-1, :-1] + mer[:-1, 1:] + mer[1:, :-1] + mer[1:, 1:])
    mer_c = np.append(mer_c.transpose(), [mer_c[:, 0]], axis=0).transpose()

    return mer_c
