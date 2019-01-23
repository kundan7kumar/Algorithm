# List and it's iteration
# Add element in the list
a=[]
for i in range(1,11):
    a.append(i)

print(a)

# With the list comprehension

b=[j for j in range(1,11)]
print(b)

#adding same element in the list

c=[1]*10
print(c)



# common element between two list

a1=[2,4,56,87,23,786,56,98]
b1=[2,34,56,7,56,67]
res=[]
for k in a1:
    if k in b1:
        res.append(k)

#With list comprehension
# one way
[res.append(i) for i in a1 if i in b1]

#2nd way
res=[i for i in a1 if i in b1]

# if some number repeated in any of the list , set
res = set(a1) & set(b1)
print(res)

