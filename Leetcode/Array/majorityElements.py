def majorityElement(A):
    count=0
    c=len(A)/2
    for i in range(len(A)):
        for j in range(len(A)-1):
            if A[i]==A[j]:
                count+=1
                j+=1
        i+=1

        if count > c:
            return A[i]

print(majorityElement([3,2,3]))