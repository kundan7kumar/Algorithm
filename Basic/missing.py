#You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

#using Sum formula
def missing(nums):
    n=len(nums)
    total=((n+1)*(n+2))/2
    sum_nums=sum(nums)
    missing_num=total-sum_nums

    return missing_num

nums = [1, 2, 4, 5, 6]
miss = missing(nums)
print(miss)
# time omplexity : O(n)
# Note : Overflow can happen if data is large:

#Xor gate

def missing_xor(nums):
    n = len(nums)
    x1 = nums[0] # For xor of all the elements in array
    x2 = 1 # For xor of all the elements from 1 to n+1
    for i in range(n):
        x1 ^= nums[i]
    for i in range(n+2):
        x2 ^= i
    return x1^x2

nums = [1, 2, 4, 5, 3, 6, 8]
miss1 = missing_xor(nums)
print(miss1)

# time complexity: O(n)

#brute force

def missing_brute(nums):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)-1):
            if nums[j]!=nums[i]:
                return j

            else:
                return 0

nums = [1, 2, 4, 5, 3, 6, 8]
miss2 = missing_xor(nums)
print(miss2)

# time Complexity: : O(n^2)
