def calculate_bmi(weight,height):
    print("Height = "+ str(height))
    print("Weight = "+ str(weight))
    bmi = weight/(height*height)
    print("Your BMI is " + str(bmi))

    if(bmi<18.5):
        print("You are underweight")
        return -1
    elif(bmi>25.0):
        print("You are overweight")
        return 0
    else:
        print("You are normal weight")
        return 1

