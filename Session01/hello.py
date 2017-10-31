print("ax^2 + bx + c = 0")
a = int(input("a = ?"))
b = int(input("b = ?"))
c = int(input("c = ?"))

delta = b*b - 4 * a * c
a_2 = (2 * a)
if delta < 0:
    print("No solution")
elif delta == 0:
    x = -b/a_2
    print("One solution:", x)
else:
    delta_root = delta ** 0.5
    x1= (-b + delta_root)/a_2
    x2= (-b - delta_root)/a_2
    print("Two solutions: x1={0}, x2={1}".format(x1, x2))
