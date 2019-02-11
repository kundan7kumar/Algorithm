#Empty String
A=""
print(A)
#Intialized with Hello
B="Hello"
#Accessing the ith element
#B[i]
print(B[2])
#Adding chars to the string :O(n) operation and a new copy is created

A = A + "Hello"
print(A)
#Alternative way to add

l = []
l.append('string1')
l.append('string2')
l.append('string3')
A = ''.join(l)

#Size of the string:// O(1)
len(A)
