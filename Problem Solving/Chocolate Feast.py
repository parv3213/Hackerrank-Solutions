#!/bin/python3

import math
import os
import random
import re
import sys

def chocolateFeast(n, c, m):
    totalChocolates = 0
    initialChocolates = int(n/c)
    totalChocolates += initialChocolates
    wrappers = totalChocolates
    wrapperExc = int(initialChocolates/m)
    while (wrapperExc >= 1):
        totalChocolates += wrapperExc
        wrappers -= wrapperExc*m
        wrappers += wrapperExc
        wrapperExc = int(wrappers/m)
        
    return totalChocolates

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
