#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
counter = 0
for i in range(0, n-1):
    for j in range(0, n-1):
        if a[j] > a[j+1]:
            counter += 1
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print("Array is sorted in " + str(counter) + " swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[n-1]))
