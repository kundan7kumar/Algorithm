# def sortedSquare(A):
#     for i in A:
#         A=i**2
#         print(sorted(A))
#
# A=[-4,-1,0,3,10]

def sortedSquare(A):
    i=0;j=len(A)-1; res=[]
    while (i<=j):
        if abs(A[i])>abs(A[j]):
            res.append(A[i]**2)
            i +=1

        else:
            res.append(A[j]**2)
            j -=1


    return res[::-1]

print(sortedSquare([-4,-1,0,3,10]))




# class Solution(object):
#     def sortedSquares(self, A):
#         N = len(A)
#         # i, j: negative, positive parts
#         j = 0
#         while j < N and A[j] < 0:
#             j += 1
#         i = j - 1
#
#         ans = []
#         while 0 <= i and j < N:
#             if A[i]**2 < A[j]**2:
#                 ans.append(A[i]**2)
#                 i -= 1
#             else:
#                 ans.append(A[j]**2)
#                 j += 1
#
#         while i >= 0:
#             ans.append(A[i]**2)
#             i -= 1
#         while j < N:
#             ans.append(A[j]**2)
#             j += 1
#
#         return ans