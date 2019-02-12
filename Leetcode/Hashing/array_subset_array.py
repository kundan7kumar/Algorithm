def isSubset(arr1,arr2,m,n):
# For two loops method
    for i in range(n):
        for j in range(m):
            if arr2[i]==arr1[j]:
                break

            if(j==m):
                return 0

        return 1

# Using python Set
    set(arr1).issuperset(arr2)

    return True


if __name__ == "__main__":

    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]

    m = len(arr1)
    n = len(arr2)

    if (isSubset(arr1, arr2, m, n)):
        print("arr2[] is subset of arr1[] ")
    else:
        print("arr2[] is not a subset of arr1[]")









# Method 4 (Use Hashing)
# 1) Create a Hash Table for all the elements of arr1[].
# 2) Traverse arr2[] and search for each element of arr2[] in the Hash Table. If element is not found then return 0.
# 3) If all elements are found then return 1.
#
#
# Method 3 (Use Sorting and Merging )
# 1) Sort both arrays: arr1[] and arr2[] O(mLogm + nLogn)
# 2) Use Merge type of process to see if all elements of sorted arr2[] are present in sorted arr1[].
#
# Method 2 (Use Sorting and Binary Search)
#
# 1) Sort arr1[] O(mLogm)
# 2) For each element of arr2[], do binary search for it in sorted arr1[].
#          a) If the element is not found then return 0.
# 3) If all elements are present then return 1.
