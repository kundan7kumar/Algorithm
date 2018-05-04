#To find the sum of list
# By iteration method
def SumList(list):
    sum=0
    for i in list:
        sum=sum+i

    return sum

print(SumList([1,2,3]))

# By recursion

def listsum(numList):
    if len(numList)==1:
        return numList[0]
    else:
        return numList[0]+listsum(numList[1:])

print(listsum([1,2,3]))