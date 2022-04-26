#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(1, 10):
        num2 == num1 + 1
        if num1 == 8 and num2 == 9:
            print("{}{}".format(num1, num2))
            break
        elif num1 != num2 and num2 > num1:
            print("{}{}, ".format(num1, num2), end="")
