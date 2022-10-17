print("Itaration")
l=[10,20,30,40,50,60]
t=len(l)

for i in range(t):
    print(l[i])

print("*****")
for i in l:
    print(i)
del(l[2])
print(l)
print(l.pop(2))
print(l)
# remove
l.remove(60)
print(l)
# # clear
# l.clear()
# print(l)

# Updated
l[0]=11
print(l)

# insert
l.insert(0, 10)
print(l)

# append
l.append(70)
print(l)

# extend
n=[33,34]
l.extend(n)
print(l)


