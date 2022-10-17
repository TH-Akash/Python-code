print("Queue")

list = []
while True:
    c = int(input('''
          1 Push Element
          2 Pop First Elements
          3 Front Element
          4 Last Element
          5 Display Stack
          6 Exit
          '''))
    if c == 1:
        n = input("Enter the value : ")
        list.append(n)
        print(list)
    if c == 2:
        if len(list) == 0:
            print("Empty Queue")
        else:
            del list[0]
            print(list)

    elif c == 3:
        if len(list) == 0:
            print("Empty Queue")

        else:

            print("First Queue Value ", list[0])
    elif c == 4:
        if len(list) == 0:
            print("Empty Queue")

        else:
            print("Last Queue Value ", list[-1])

    elif c == 5:
        print("Display Queue", list)

    elif c == 6:
        break;

    else:
        print("Invalid opr......")
