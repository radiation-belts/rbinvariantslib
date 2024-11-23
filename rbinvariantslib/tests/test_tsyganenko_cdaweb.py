from datetime import datetime

from rbinvariantslib import models


def test_single_time():
    """Test calling get_tsyganenko_params() with a single time"""
    time = datetime(2013, 10, 2, 13, 5)
    params = models.get_tsyganenko_params(time)
    expected = {'Pdyn': 5.460000038146973, 'SymH': -56.0,
                'By': -1.0700000524520874, 'Bz': 5.579999923706055}

    for key, value in params.items():
        assert isinstance(value, float)
        assert abs(value - expected[key]) < .1

        
def test_multiple_times():
    """Test calling get_tsyganenko_params() with multiple times"""    
    times = [
        datetime(2013, 10, 2, 13, 5),
        datetime(2013, 10, 2, 13, 10),
        datetime(2013, 10, 2, 13, 15),
    ]
    params_dict_list = models.get_tsyganenko_params(times)

    expected = [
        {'Pdyn': 5.460000038146973, 'SymH': -56.0,
         'By': -1.0700000524520874, 'Bz': 5.579999923706055},
        {'Pdyn': 4.889999866485596, 'SymH': -56.0,
         'By': 2.430000066757202, 'Bz': 3.7200000286102295},
        {'Pdyn': 4.800000190734863, 'SymH': -56.0,
         'By': -1.2699999809265137, 'Bz': 4.159999847412109}
    ]

    assert len(params_dict_list) == len(expected), \
        'Params list not expected length'
    
    for got_dict, expected_dict in zip(params_dict_list, expected):
        assert len(got_dict) == len(expected_dict), \
            'Dict has unexpected number of keys' 
        
        for key, got_value in got_dict.items():
            assert isinstance(got_value, float)
            assert abs(got_value - expected_dict[key]) < .1
