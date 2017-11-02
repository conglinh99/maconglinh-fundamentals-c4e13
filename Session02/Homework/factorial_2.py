n = int(input("Input factorial you want to calculate: "))

val = 1

if n < 0:
    print("You must enter a positive number!")
else:
    for i in range(1, n+1, 1):
        val *= i
    print("Value of the factorial: ", val)
