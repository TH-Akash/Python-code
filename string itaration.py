print("String Iteration")

w="Welcome to python course"
t=len(w)
for i in range(t):
    print(w[i])

# reverse

print("------")
for i in range(t-1,-1,-1):
    print(w[i])

print("Lower")
# lower()
lo = w.lower()
print(lo)

# Upper()
print("Upper")
up=w.upper()
print(up)

# capital
print("capitalize")
ca=w.capitalize()
print(ca)

# title()
print("Title")
ta=w.title()
print(ta)

# find()
print("Find")
a="akash123"
print(a.find('as',2))

# index()
print("index")
print(a.index('s',2))

# isalpha()
print("isalpha")
print(a.isalpha())

# isdigit()
w="4444"
print(w.isdigit())

# isalnum()
w="sdj444"
print(w.isalnum())

w="sdj44@4"
print(w.isalnum())