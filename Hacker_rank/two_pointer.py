class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        temp = []
        a = 0
        for i in range(len(A)):
            temp.append(0)
        for i in range(len(A)):
            if temp[A[i] - 1] == 0:
                temp[A[i] - 1] = 1
                continue
            else:
                if temp[A[i] - 1] == 1:
                    temp[A[i] - 1] = 2
                    a = A[i]
                    continue

        b = 0
        for i in range(len(A)):
            if temp[i] == 0:
                b = i + 1
        return a, b

    # hashNum = {}

    # for i in nums:
    #     if i not in hashNum:
    #         hashNum[i] = 1
    #     else:
    #         return True
    # return False

    # Method 2 -- Sorting
    # l =  len(nums)
    # if l < 2:
    #     return False
    # nums.sort()
    # for i in range(l-1):
    #     if nums[i] == nums[i+1]:
    #         return True
    # return False

    # Method 3 -- Set solution for python
    numsSet = set(nums)
    if len(nums) == len(numsSet):
        return False
    return True

