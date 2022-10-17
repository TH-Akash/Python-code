l=[1,2,3,4,5,6]
li=[3,4,5,6,76,7]

t=len(l)
for a,b in zip(l,li):
    print(a,b)


for h in range(t):
    print(l[h],li[h])


# string Convert  list
n=input("rnter the input :  ")
sp=n.split()
print(sp)

# string convert to list
stringList=[]
n=int(input("Enter the number loop : "))
for a in range(1,n+1):
    n1=input("Enter the string value "+str(a)+":-")
    stringList.append(n1)
print(stringList)

