import Lab2

def test_find_min_max():
    min_max = [1,3]
    temp_list = [1,2,3]
    min = Lab2.calc_min_max_temperature(temp_list)
    assert (min_max == [1,3])



def test_calc_average():
    result = 2
    temp_list = [1,2,3]
    result =Lab2.calc_average_temperature(temp_list)
    assert (result == 2)

def test_calc_median_temp():
    result = 2
    temp_list = [1,2,3]
    result =Lab2.calc_median_temperature(temp_list)
    assert (result == 2)