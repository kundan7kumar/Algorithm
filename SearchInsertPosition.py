"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

        return len([x for x in nums if x<target])
        class Solution:
    def searchInsert(self, nums, target):
        return bisect.bisect_left(nums, target)
"""

class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return l
