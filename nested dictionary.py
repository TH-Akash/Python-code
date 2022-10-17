print("Nested Dictionary")

course={
    'php':{'time':'3 Month','fees':1000},
    'Java':{'time':'2 Month','fees':1400},
    'Python':{'time':'3 Month','fees':1000},
}
print(course)
course['Java']['fees']=2000
print(course['php']['fees'])
print("----")
for k,v in course.items(): # All dictionary print
     print(k, v['time'], v['fees'])