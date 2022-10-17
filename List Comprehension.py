print("List Comprehension")

l = [n for n in range(1, 11)]
print(l)

#  filter
n = [h for h in range(1, 21) if h % 2 == 0]
print(n)

# string
s="Akash"
d=[g for g in (s)]
print(d)

# count()
list1 = [1,2,33,4,4,5,5,5,6]
a=list1.count(5)
print(a)

# max()
m=max(list1)
print(m)
n=["Akash","hello"]
print(max(n))

# min()
mn=min(list1)
print(mn)
n=["Akash","hello"]
print(min(n))

# sort()
s=sorted(list1)
print(s)

# revers
list1.reverse()
print(list1)

# index
i=list1.index(33)
print(i)
