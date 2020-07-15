#!/bin/python3

import sys


S = input().strip()
# S = "3"

try:
    print(int(S))
except:
    print("Bad String")
