import numpy as np
n=4
m=3
p=2
lsi=[]
for i in range(n+m):
    inp=raw_input().split()
    lsi.append(inp)

print(np.array(lsi,int))