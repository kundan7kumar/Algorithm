# def sortArrayParity(A):
#     res=[a for a in A if not a % 2] + [a for a in A if a % 2]
#     return res
    # res=[]
    # for i in range(len(A)):
    #     if A[i]/2==0:
    #         res.append(A[i])
    #
    #     else:
    #         res.append(A[i])
def sortArrayByParity(A):

    i, j = 0, len(A) - 1
    while i < j:
        if A[i] % 2 > A[j] % 2:
            A[i], A[j] = A[j], A[i]

        if A[i] % 2 == 0: i += 1
        if A[j] % 2 == 1: j -= 1

    return A
print(sortArrayByParity([3,1,2,4]))


    # A.sort(key = lambda x: x%2)
    #     return A
