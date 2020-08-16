#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    arr = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        r = re.compile("[a-zA-Z.]+@gmail.com$")
        result = r.match(emailID)
        if result is not None:
            arr.append(firstName)
    arr.sort()
    for i in range(len(arr)):
        print(arr[i])
