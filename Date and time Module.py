print("DateTime Module")

import datetime
x=datetime.datetime.now()
print(x)

# yr-mn-date
x=datetime.datetime(2022,10,21)
print(x)

# steftime()
x=datetime.datetime.now()
y=x.strftime("%I")
print(y)
