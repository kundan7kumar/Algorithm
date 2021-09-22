"""Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""
def intersectionarray(nums1,nums2):
    int_array =[]
    for i in range(0,len(nums1)):
        for j in range(0,len(nums2)):
            if nums1[i]==nums2[j]:
                if nums1[i] not in int_array:
                    int_array.append(nums1[i])
    return int_array

"Time Complexity : O(m*n) , Space Complexity= O(1):doubt"

def intersectionarray1(nums1,nums2):
    set1= set(nums1)
    set2 =set(nums2)
    return list(set2 & set1)
"Time Complexity : average O(m+n), worst: O(m*n)"

class Solution:
    def set_intersection(self, set1,set2):
        return [ x for x in set1 if x in set2]


    def  intersectionarray2(self, nums1,nums2):
        set1=set(nums1)
        set2=set(nums2)
        if len(set1)<len(set2):
            return self.set_intersection(set1,set2)
        else:
            return self.set_intersection(set2,set1)