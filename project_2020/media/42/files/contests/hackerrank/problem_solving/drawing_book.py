#!/bin/python

from __future__ import print_function

import os
import sys

def pageCount(n, p):
    from_front = p//2
    from_back = (n-p)//2 if n % 2 else (n-p+1)//2
    return min(from_front, from_back)

if __name__ == '__main__':
    n = int(input())
    p = int(input())
    print(pageCount(n, p))
