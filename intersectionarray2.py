"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

"""
def intersectionarray2(nums1,nums2):
    from collections import Counter
    num1 = Counter(nums1)
    num2 = Counter(nums2)
    return list((num1 & num2).elements())


