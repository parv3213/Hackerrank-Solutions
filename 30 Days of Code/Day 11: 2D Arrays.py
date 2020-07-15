#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    a = 0
    b = 0
    c = 0
    d = 0
    total = 0
    maxTotal = -63

    for a in range(4):
        for b in range(4):

            for c in range(a, a+3):
                for d in range(b, b+3):
                    if (c == a+1 and d == b) or (c == a+1 and d == b+2):
                        continue
                    total = total + arr[c][d]

            if (maxTotal < total):
                maxTotal = total
            total = 0
    print(maxTotal)
