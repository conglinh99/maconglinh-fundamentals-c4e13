from random import randint

# count = 0
while True:
    n = int(input("Guess my number? (1-100)"))
    n = randint(1, 100)
    if n > 20:
        print("Too large =))")
    elif n == 13:
        print("Exactly!")
    elif n < 13:
        print("Smaller!")
    else:
        print("Nearly")
            # count += 1
