"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

# For Two Loop: O(n^2)

def containsDuplicate(nums):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

# For One Loop: O(n)
def containsDuplicate1(nums):
    nums.sort()
    for i in range(0, len(nums)):
        if nums[i] == nums[i + 1]:
            return True

# check length of length of elements
def containsDuplicate2(nums):
    if len(set(nums)) < len(nums):
        return True
    else:
        return False

# Using Hash
def containsDuplicate3(nums):
    dict = {}
    for i in nums:
        if i in dict:
            return True
        else:
            dict[i] = True

    return False

nums=[1, 2, 3, 1]
#print(nums)
