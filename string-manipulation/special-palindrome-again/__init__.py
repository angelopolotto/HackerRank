#!/bin/python3

import math
import os
import random
import re
import sys
from timeit import default_timer as timer
from collections import Counter

# Complete the substrCount function below.
def substrCount(n, s):
    igual_p = Counter(s)
    print(igual_p)
    s_palindrome = sum(igual_p.values())

    print(s_palindrome)

    i = 3
    while i < n:
        for j in range(n-i):
            sub_s = s[j:j+i]
            print(sub_s)
            if  sub_s == sub_s[::-1]:
                s_palindrome += 1
        i += 2
    
    return s_palindrome


def substrCountSolution1(n, s):
    s_palindrome = n
    i = 0
    for i in range(1, n):
        for j in range(n - i):
            sub_s = s[j:j+i+1]
            if  sub_s == sub_s[::-1]:
                freq = Counter(sub_s)
                len_freq = len(freq)
                
                if len_freq == 1:
                    s_palindrome += 1
                else:    
                    N = len(sub_s)
                    if len_freq == 2 and N % 2 != 0 and sub_s[N//2] != sub_s[0]:
                        s_palindrome += 1
    
    return s_palindrome
                    
        
if __name__ == '__main__':
    start = timer()
    test_case = '16'
    scr_dir = os.path.dirname(__file__)
    fptr = open(os.path.join(scr_dir, './output/output.txt'), 'w')
    fptr_in = open(os.path.join(scr_dir, './input/input%s.txt' % test_case), 'r')
    fptr_test = open(os.path.join(scr_dir, './output/output%s.txt' % test_case), 'r')

    n = int(fptr_in.readline().rstrip())

    s = fptr_in.readline().rstrip()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

    test_result = int(fptr_test.readline())
    print(result, test_result, result == test_result, timer() - start)
