print("set ")

l=[1,2,3]
s=set(l)
print(s)

# add
s={10,20,30,50,60}
s.add(40)
print(s)

# Pop()
print(s.pop())
print(s)

# remove()
s.remove(20)
print(s)

# discard
s.discard(10)
print(s)

# update()
up=[70,80]
s.update(up)
print(s)

# clear()
s.clear()
print(s)
