#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    t = int(input())

    def findMaxAnd(n, k):
        maxAnd = 0
        for i in range(n-1, 0, -1):
            for j in range(n, i, -1):
                andNo = i & j
                if (andNo < k and maxAnd < andNo):
                    maxAnd = andNo
                    if maxAnd == k-1:
                        return maxAnd
        return maxAnd

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        print(findMaxAnd(n, k))
