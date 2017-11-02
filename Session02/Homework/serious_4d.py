r = int(input("Enter number of row you want: "))
c = int(input("Enter number of column you want: "))

for i in range(r):
    if i % 2 == 0:
        for y in range(c):
            print("x ", end= "* ")
        print()    
    else:
        for y in range(c):
            print("* ", end= "x ")
        print()
