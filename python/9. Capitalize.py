#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    resStr = ""
    for i in range(len(s)):
        if s[i-1]  == " " or i==0:
            resStr += s[i].upper()
        else:
            resStr += s[i]
    return resStr


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result + '\n')

    # fptr.write(result + '\n')

    # fptr.close()
