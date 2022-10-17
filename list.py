# Mutable
# []
# multiple value

print("List")

l=[1,2,4,5,6,"hello",[7,8,9]]
print(type(l)) # class List

#index
print(l[2])

# 5 , hello
print(l[3],l[5])

# [7,8,9]=[8]
print(l[6][1])

#  slice 1,2
print(l[0:2])

# slice 1,4,6,[7,8,9]
print(l[0::2])

# [5,6,"hello",[7,8,9]]
print(l[3:])

# [1,4,6,[7,8,9]]
print(l[-1::-2])

# [1,2,4,5,6,"hello",[7,8,9]]
print(l[-1::-1])