from rbinvariantslib import models, invariants
from datetime import datetime
import numpy as np

import testing_utils


def test_tsyganenko():
    # Get TS05 model input parameters
    time = datetime(2015, 10, 2)
    params = models.get_tsyganenko_params(time)

    # Evaluate TS05 model on regular grid
    axis = np.arange(-10, 10, 0.5)
    x, y, z = np.meshgrid(axis, axis, axis)
    model = models.get_tsyganenko(
        "TS05", params, time,
        x_re_sm_grid=x,
        y_re_sm_grid=y,
        z_re_sm_grid=z,
        inner_boundary=1.5
    )

    # Calculate L*
    result = invariants.calculate_LStar(
        model,
        starting_point=(-6.6, 0, 0),
        starting_pitch_angle=60
    )
    
    assert abs(result.LStar - 5.79) < .1


def test_swmf():
    fname = testing_utils.get_swmf_file()
    
    model = models.get_model(
        "SWMF_CDF",
        fname
    )

    result = invariants.calculate_K(
        model,
        starting_point=(-6.6, 0, 0),
        mirror_latitude=50
    )
    
    assert abs(result.K - 1.7) < .1
