teen_dict = {
    'cj': 'Chị'
    'pts': 'Photoshop'
    'eny': 'Em người yêu'
}

while True:

    print(*teen_dict)
    code = input("Your code?")
    if code in teen_dict:
        print(teen_dict[code])
    else:
        print("Not found")
        choice = input("Do you want to contribute? (Y/N)").upper
        if choice == "Y":
            Translation = input("Your translation:")
            teen_dict[code] = translation
            print("Updated!")
