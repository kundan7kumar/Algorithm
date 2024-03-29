"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

"""

""" This exceeded the time limit"""

# import bisect
# class Solution():
# def firstBadVersion(self, n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     self.__getitem__ = isBadVersion
#     return bisect.bisect_left(self, True, 1, n)


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n):
            if isBadVersion(i)==True:
                return i
        return n

""" Binary Search Solution"""


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
### Need to understand the time exceed avoid

"""https://www.reddit.com/r/Python/comments/36xu5z/can_integer_operations_overflow_in_python/
"""
