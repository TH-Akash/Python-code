print("Dictionary")

d={
    'name':"akash",
    'fec':'8000',
    'duratuion':'2 Month'


}
for n in d:
    print(d[n])  # value return
print(type(d))
f=d['fec']
print(f)

# get()
v=d.get('name')
print(v)
print("----")
# keys()
for n in d.keys():
    print(n)

print("__")
# value

for n in d.values():
    print(n)

# items()
for a,b in d.items():
    print("ITEMS : ",a,b)

# del
del d['fec']
print(d)

# pop()
print(d.pop('duratuion'))
print(d)

# dict()
d=dict(name='Python',fees='8000') # dictionary create
print(d)

# update()
d={
    'name':"akash",
    'fec':'8000',
    'duratuion':'2 Month'
}
d.update({'fec':100000})
print(d)

# # clear()
# d.clear()
# print(d)
d['desc']="this Python"
print(d)
d['fec']=10000
print(d)