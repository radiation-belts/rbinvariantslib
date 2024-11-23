from rbinvariantslib import models, invariants
import testing_utils


def test_lfm():
    """Test calculating an Lstar with LFM"""
    fname = testing_utils.get_lfm_file()

    model = models.get_model(
        "lfm_hdf4",
        fname
    )
    
    # Calculate L*
    result = invariants.calculate_LStar(
        model,
        starting_point=(-6.6, 0, 0),
        starting_pitch_angle=60
    )

    expected = 6.627379641675664
    assert abs(result.LStar - expected) / expected < .05

    
