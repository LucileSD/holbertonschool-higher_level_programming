#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        ch = ord(str[i])
        if ch > 96 and ch < 123:
            ch = ch - 32
        result = chr(ch)
        print(result, end="")
    print()
