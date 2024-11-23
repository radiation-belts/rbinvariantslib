from rbinvariantslib import models
import testing_utils


def test_lfm_interpolate():
    """Test interpolating LFM"""
    fname = testing_utils.get_lfm_file()
    model = models.get_model(
        "lfm_hdf4",
        fname
    )
    
    B_got = model.interpolate((-5, 0, 0))
    B_expected = (-5.510784852447146e-06,
                  -2.583930850175165e-06,
                  0.0025205996644217495)

    assert len(B_got) == len(B_expected)
    assert abs(B_got[0] - B_expected[0]) < 1e-5
    assert abs(B_got[1] - B_expected[1]) < 1e-5
    assert abs(B_got[2] - B_expected[2]) < 1e-3


def test_get_dipole_on_lfm_grid():
    """Tests calculating dipole on LFM grid and interpolating value"""
    fname = testing_utils.get_lfm_file()
    model = models.get_dipole_model_on_lfm_grid(fname)

    B_got = model.interpolate((-5, 0, 0))
    B_expected = (6.779802670800632e-13,
                  3.559951359809801e-21,
                  -0.0024758772204116035)

    assert len(B_got) == len(B_expected)
    assert abs(B_got[0] - B_expected[0]) < 1e-5
    assert abs(B_got[1] - B_expected[1]) < 1e-5
    assert abs(B_got[2] - B_expected[2]) < 1e-3

