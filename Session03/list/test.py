from random import choice

s = "confusing"
characters = list(s)
n = len(s)
l = []
count = 1
for i in range(n):
    c = choice(characters)
    l.insert(i,c)
    characters.remove(c)
print(*l)

while count <= 7:
    enter = input("Enter your answer: ")
    if enter == s:
        print("Congratulations!")
        break
    else:
        print("You're wrong!")
        count += 1

print("The right answer is", s)
