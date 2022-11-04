import calcbmi

def test_bmi_normal_weight():
    result = 0
    Height=1.78
    Weight=79

    result = calcbmi.calculate_bmi(Weight,Height)

    assert (result==1)


def test_bmi_over_weight():
    result = 1
    Height=1.78
    Weight=790

    result = calcbmi.calculate_bmi(Weight,Height)

    assert (result==0)



def test_bmi_under_weight():
        result = -1
        Height = 1.78
        Weight = 10

        result = calcbmi.calculate_bmi(Weight, Height)

        assert (result == -1)


