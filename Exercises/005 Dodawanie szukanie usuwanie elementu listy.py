list1 = []
while(True):
    action = (input("Select an action + add, - remove, / serach, other - end: "))
    if (action == "+") or (action == "-") or (action == "/"):
        item = (input("Enter item to add, remove or search: "))
        if (action == "+"):
            list1.append(item)
        elif (action == "-"):
            if (list1.count(item) == 1):
                list1.remove(item)
            else:
                print("Item is not on the list")
        elif (action == "/"):
            if (list1.count(item) == 1):
                print("Item is on the list")
            else:
                print("Item is not on the list")
        print("The list includes the following items: ", list1)
    else:
        print("End")
        break
