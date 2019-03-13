# Compute Subproblem Separately and combine them
#Avoid global variable
# No passing through a result array


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1)+fib(n-2)

#Time Complexity = O(2^n)

for n in range(1,11):
    print(n, ':', fib(n))

# Store value in data structure and use it

# Memoization: 1.
fibonacci_cache ={}

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1)+fib(n-2)

#Recursion + Caching = dynamic programming﻿



#
#
#
# print(fib(4))

''' Given an integer n, write a function that will return the nth Fibonacci number.
eg.
*fib(0) = 0
*fib(1) = 1
*fib(5) = 5
*fib(10) = 55

// We will assume for all solutions that n >= 0 and that int is sufficient to hold the result

'''
# Top down approach


# Bottom Up approach

#https://stackoverflow.com/questions/6164629/what-is-the-difference-between-bottom-up-and-top-down
# I personally find memoization much more natural.
# You can take a recursive function and memoize it by a mechanical process
# (first lookup answer in cache and return it if possible, otherwise compute it recursively and then
# before returning, you save the calculation in the cache for future use), whereas doing bottom up dynamic programming
# requires you to encode an order in which solutions are calculated, such that no "big problem" is computed before the smaller
# problem that it depends on.