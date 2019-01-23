# Normal list iteration

data=['1','3','4','7','8',None,'11','28',None,'27','98']
result=[]
for i in data:
    if i!= None:
        result.append(float(i))

    else:
        result.append(0)

print(result)


# With list Comprehension

result=[(float(i)) if i!=None else 0 for i in data]

print(result)

#Other Way

result=[float(i or 0) for i in data]

print(result)