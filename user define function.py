print("User define function")

# simple function
def simplefunction():
    print("Welcome to ws")

simplefunction()


# function with Argument()

def sum(a,b):
    print(a+b)

sum(3,5)
sum(10,30)

# argument with defolt value


def sumdata(a,b=5):
    print(a*b)

sumdata(20)

# return function
def sumReturnFunction(a,b=10):
    c=a+b
    return c

oputut = sumReturnFunction(20)
print(oputut)
