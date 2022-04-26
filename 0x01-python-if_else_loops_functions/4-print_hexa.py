#!/usr/bin/python3
for dec in range(0, 99):
    h = hex(dec)[2:]
    print("{} = 0x{}".format(dec, h))
