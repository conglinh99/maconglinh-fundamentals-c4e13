alphabet_dict = {
    'a': 2,
    'c': 1,
    'd': 1,
    'e': 5,
    'g': 1,
    'h': 2,
    'i': 4,
    'l': 2,
    'n': 2,
    'o': 1,
    'p': 2,
    'r': 4,
    's': 5,
    't': 5,
    'u': 1,
    'w': 2
}
user = input("What do you find? ").lower()
if user in alphabet_dict:
    print(alphabet_dict[user])
else:
    print("Not found!")
