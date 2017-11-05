# menu = []
# print(menu)
# menu = ['chan gia xao ot']
# print(menu)

menu = ['chan gia sa ot' , 'ga xao pho mai' , ' com rang dua bo']

print(*menu, sep=', ')

n = input('what do you want to add?')

menu.append(n)

print(*menu, sep=', ')
