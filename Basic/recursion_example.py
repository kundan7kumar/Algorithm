# recursion : a function is recursive if it calls itself and have termination condition
# recursion includes atleast two parts. a. a base condition b. at least one recursive case
# E.g : Add all elements in the list

#Without recursion

def add(list):
    add=0
    for i in range(0,len(list)):
        add=add+list[i]

    return add

print add([3,5,7,9])

# with recursion

def sum(list):
    if len(list)==1:

        return list[0]

    else :
        return list[0]+sum(list[1:])

print add([3,5,7,9])

# Without recursion

def itr_fact(n):
    sum1 = 1
    for i in range(2,n+1):
        sum1 *= i
    return sum1

print itr_fact(3)

# factorial with recursion

import sys

sys.setrecursionlimit(3000) # if program crashes , we have set a limit
def fact(n):

    if n==1:
        return 1
    else:
        return n*fact(n-1)

print fact(2000)



