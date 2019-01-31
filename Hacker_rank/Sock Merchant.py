



from collections import Counter
input()
socks, pairs = Counter(map(int,input().strip().split())), 0
for s in socks: pairs += socks[s]//2
print(pairs)
#
#
#
# print (sum(c.count(x)//2 for x in set(c)))
#
#
import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
tot = 0
d = {}
for i in range(n):
    if c[i] in d:
        d.pop(c[i])
        tot += 1
    else:
        d[c[i]] = 1
print tot