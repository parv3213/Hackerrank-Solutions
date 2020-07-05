#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.


def dayOfProgrammer(year):
    y = year
    arr = [31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y <= 1917:
        if y % 4 == 0:
            days = 29
        else:
            days = 28
    elif y >= 1919:
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            days = 29
        else:
            days = 28
    else:
        days = 28-13

    arr.insert(1, days)
    add = 0
    i = 0
    des = 256
    while((add+arr[i]) < des):
        add += arr[i]
        i += 1
    month = i+1
    day = 256-add
    if len(str(day)) != 2:
        day = "0"+str(day)
    if len(str(month)) != 2:
        month = "0"+str(month)
    return (str(day)+"."+str(month)+"."+str(y))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
