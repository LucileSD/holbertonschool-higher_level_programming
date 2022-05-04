#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        size = 0
        sum = 0
        for i in my_list:
            sum += i[0] * i[1]
            size += i[1]
        return sum / size
    else:
        return 0
