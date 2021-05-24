#!/bin/python3

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    minimum = min(a)
    maximum = max(b)
    count =0
    arr=[]
    crr=[]
    for i in range (minimum,maximum+minimum,minimum):
        for j in a:
            if i % j == 0 :
                count += 1
            if count ==len(a):
                arr.append(i)
        count=0
    for i in arr:
        for j in b:
            if j%i==0:
                count += 1
        if count== len(b):
            crr.append(i)
        count=0
    return len(crr)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
    print(total)
