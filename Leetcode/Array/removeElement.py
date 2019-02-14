def removeElement(nums,val):
    if not len(nums):
        return 0
    l=0

    for i in range(len(nums)):
        if nums[i]!=val:
            nums[l]=nums[i]
            l+=1


    return l

print(removeElement([3,2,2,3],3))