def isArraySorted(n):
    if len(n)==1:
        return True
    else:
        return n[0]<=n[1] and isArraySorted(n[:1])

n=[527,240,246,277,321,454]

print(isArraySorted(n))