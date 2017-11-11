from random import choice

words = ['lion','vainglory','pizza', 'tiger']

answer = choice(words)

quizz = []
for i in range(len(answer)):
    quizz.insert(i, '_ ')
print(*quizz)

key = list(answer)

guess_time = 0
loop_continue = True

while loop_continue:
    guess_time = input("Guess a character? ")

    if guess_time in key:

        for i in range(len(answer)):
            if guess_time == key[i]:
                quizz[i] = key[i]

    else:
        guess_time += 1

        if guess_time == 1:
            print(
            """
             ----------
             |        O
             |
             |
             |
            _|_
            """
            )
        elif guess_time == 2:
            print(
            """
             ----------
             |        O
             |        |
             |
             |
            _|_
            """
            )
        elif guess_time == 3:
            print(
            """
             ----------
             |        O
             |       -|
             |
             |
            _|_
            """
            )
        elif guess_time == 4:
            print(
            """
             ----------
             |        O
             |       -|-
             |
             |
            _|_
            """
            )
        elif guess_time == 5:
            print(
            """
             ----------
             |        O
             |       -|-
             |       /
             |
            _|_
            """
            )
        elif guess_time == 6:
            print(
            """
             ----------
             |        O
             |       -|-
             |       / \\
             |
            _|_
            """
            )
            print("You failed!")
            loop_continue = False
    print(*quizz)
    if quizz == key:
        print("Congratulations!")
        loop_continue = False
