def display_main_menu():
    print("Enter some number separated by commas (e.g. 5, 67, 32)")

def calc_average():
    print("calc_average")

def get_user_input():
    i = input()
    list = i.split(",")
    for i in list:
        i = float(i)
    return list

def calc_average_temperature(temp_list):
    avgtemp = 0
    for x in temp_list:
        avgtemp += float(x)/len(temp_list)
    print("Average temp: " + str(avgtemp))
    return avgtemp

def calc_min_max_temperature(temp_list):
       list(map(float, temp_list))
       print(min(temp_list),max(temp_list))

def calc_median_temperature(temp_list):
    temp_list.sort(key= float)
    print(temp_list)
    length = len(temp_list)
    if length%2 == 0:
        x = int(length/2)
        median = (float(temp_list[x-1])+float(temp_list[x]))/2
    else:
        median = temp_list[int((length-1)/2)]
    print("Median: " + str(median))
    return median

def main():
    print ("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_median_temperature(num_list)
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)





if __name__ == "__main__":
    main()