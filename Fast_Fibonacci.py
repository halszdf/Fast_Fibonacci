#!/usr/bin/python
# -*- coding: utf-8 -*-
# Fast fibonacci algorithm
# Created By Hals Halil Sayarsoy 7.June.2019
# Turkey / Istanbul

import os
import shutil
import stat
import errno
import time
import datetime
import argparse
import sys


def fibonacci(n, fib):
    n1 = 0
    n2 = 0
    print ('sdsdsf')
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        print ('>2--', n, fib[n - 1], fib[n - 2])
        if fib[n - 1] > 0:
            n1 = fib[n - 1]
        else:
            n1 = fibonacci(n - 1, fib)
            fib.insert(n - 1, n1)
        if fib[n - 2] > 0:
            n2 = fib[n - 2]
        else:

            n2 = fibonacci(n - 2, fib)

            # fib.insert(n-2,n2)

        return n1 + n2


def basla():
    fib = [0, 1, 2]
    n=1011
    for j in range(3, n):
        fib.insert(j, 0)

    for j in range(1, n):
        print (j, ':', fibonacci(j, fib))


def main(argv):

    # My code here

    pass


if __name__ == '__main__':
    main(sys.argv)
    basla()

			