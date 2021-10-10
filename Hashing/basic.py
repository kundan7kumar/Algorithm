# Python tuple can be the key but python list cannot

a ={1:"USA",2:"UK",3:"INDIA"}
print(a)
print(a[1])
print(a[2])
print(a[3])
#print(a[4]) # key Error

# The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict never raises a KeyError. It provides a default value for the key that does not exists.
from collections import defaultdict
d=defaultdict()
d["a"] =1
d["b"] = 2

print(d)
print(d["a"])
print(d["b"])
print(d["c"])