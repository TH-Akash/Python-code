print("Tuple")
t=(10,20,30,40)
print(t[3])

# min()
m=min(t)
print(m)

# max()
mx=max(t)
print(mx)

# index
i=t.index(30)
print(i)

# count()
c=t.count(10)
print(c)

# sum
s=sum(t)
print(s)

print("____")

l=len(t)
for n in range(l):
    print(t[n])

print("____")

for a in t:
    print(a)
