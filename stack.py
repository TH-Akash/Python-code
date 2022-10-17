print("stack")

list = []
while True:
    c = int(input('''
          1 Push Element
          2 Pop Element
          2 Pick Element
          4 Display Stack
          5 Exit
          '''))
    if c == 1:
        n = input("Enter the value : ")
        list.append(n)
        print(list)
    if c == 2:
        if len(list) == 0:
            print("Empty Stack")
        else:
            d = list.Pop()
            print(d)
            print(list)

    elif c == 3:
        if len(list) == 0:
            print("Empty Stack")

        else:
            print("Last Stack Value ", list[-1])
    elif c == 4:
        print("Display Stack", list)
    elif c == 5:
        break;
    else:
        print("Invalid ")
