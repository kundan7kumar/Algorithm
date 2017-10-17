#using brute force
class Solution(object):
    def twoSum(self, nums, target):
        for i in xrange(0,len(nums)):
            for j in xrange(i+1,len(nums)):
                if nums[j]==target-nums[i]:
                    return (i,j)
#Space Complexity : O(1)        :Time Complexity :O(n^2)


#Dictionary

class Solution(object):
    def twoSum(self, nums, target):
        twosum={}
        for i,x in enumerate(nums):
            if target-x in twosum:
                return (twosum[target-x],i)
            twosum[x]=i

# Space Complexity : O(n)        :Time Complexity :O(n)

class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[target-nums[i]] = i
            else:
                return (dict[nums[i]], i)

#two pointer Method

class Solution(object):
    def twoSum(self, nums, target):
        nums = enumerate(nums)
        nums = sorted(nums, key=lambda x: x[1])
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l][1] + nums[r][1] == target:
                return sorted([nums[l][0], nums[r][0]])
            elif nums[l][1] + nums[r][1] < target:
                l += 1
            else:
                r -= 1
