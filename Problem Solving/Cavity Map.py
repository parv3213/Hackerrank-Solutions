#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    for i in range(len(grid)):
        newString = ""
        if (i == 0 or i == (len(grid)-1)):
            continue
        for j in range(len(grid)):
            if (j == 0 or j == (len(grid)-1)):
                newString += grid[i][j]
                continue
            if (grid[i][j] > grid[i-1][j] and grid[i][j] > grid[i+1][j] and grid[i][j] > grid[i][j-1] and grid[i][j] > grid[i][j+1]):
                # print (grid[i][j])
                newString += "X"
            else:
                newString += grid[i][j]
        grid[i] = newString
    return (grid)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
