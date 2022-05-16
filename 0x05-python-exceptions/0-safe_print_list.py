#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    while x > 0:
        try:
            print(f"{my_list[count]}", end="")
            x -= 1
            count += 1
        except Exception:
            print()
            return count
    print()
    return count
