# CRUD exercise
our_items = ["T-Shirt", "Sweater"]
while True:
    n = input("Welcome to our shop, what do you want (C, R, U, D)?")
    if n.upper() == "C":
        new_item = input("Enter new item: ")
        our_items.append(new_item)
        print("Our Items:", end = ":", sep = "")
        print(*our_items, sep=", ")
    elif n.upper() == "R":
            print("Our items:", end =":", sep= "")
            print(*our_items, sep=", ")
    elif n.upper() == "U":
        update_possition = int(input("Update position?"))
        if -3 <= update_possition <= 3:
            new_item = input("New item?")
            our_items[update_possition - 1] = new_item
            print("Our items", end= ":", sep="")
            print(*our_items, sep= ", ")
        else:
            print("Out of the index!")
    elif n.upper() == "D":
        delete_position = int(input("Delete position?"))
        if -3 <= delete_position <= 3:
            del our_items[delete_position - 1]
            print("Our items", end=":", sep="")
            print(*our_items, sep=", ")
        else:
            print("Out of the index!")
    else:
        print("Out of the selection!")
        break
