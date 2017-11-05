flock = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Linh and here is my flock")
print(flock)
print()
print("Now my biggest sheep has size", max(flock),"let's shear it")
print("After shearing, here is my flock")
for index, item in enumerate(flock):
    if item == max(flock):
        flock[index] = 8
        break
print(flock)
month = 0
for i in range(2):
    month += 1
    flock = [x + 50 for x in flock]
    print("MONTH", month," :")
    print("One month has passed, now here is my flock")
    print(flock)
    print("Now my biggest sheep has size", max(flock),"let's shear it")
    print("After shearing, here is my flock")
    for index, item in enumerate(flock):
        if item == max(flock):
            flock[index] = 8
            break
    print(flock)
print("MONTH 3:")
print("One month has pass, now here is my flock")
flock = [x + 50 for x in flock]
print(flock)
print("My flock has size in total:", sum(flock))
print("I would get", sum(flock),"* 2$ =", sum(flock) * 2, "$" )
