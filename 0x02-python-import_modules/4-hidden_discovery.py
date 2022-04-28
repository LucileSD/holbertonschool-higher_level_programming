#!/usr/bin/python3
import hidden_4 as hide
if __name__ == "__main__":
    for i in range(len(dir(hide))):
        if dir(hide)[i][:2] != "__":
            print("{}".format(dir(hide)[i]))
