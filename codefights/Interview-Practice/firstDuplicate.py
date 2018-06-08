#Two Loop Method
def firstDuplicate(a):
    idx=len(a)
    flag=False
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                if idx>j:
                    idx=j
                    flag=True
                    
    if flag==True:
        return a[idx]
            
    else:
        return -1
            

# Using set
def firstDuplicate(a):
    dup = set()
    for i in a:
        if i in dup:
            return i
        dup.add(i)

    return -1
