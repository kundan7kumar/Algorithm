def single_num(nums):
    A={}
    a = 0
    for i in nums:
        a ^= i
    return a

print single_num([1,2,3,4,5,4,3,2,1])