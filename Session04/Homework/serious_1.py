inventory = {
    'gold' : [500],
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# add a key to inventory called 'pocket' and set the value.
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# remove('dagger') from the list of items stored under the 'backpack' key.
inventory['backpack'].remove('dagger')

# add 50 to the number stored under the 'gold' key.
inventory['gold'].append(50)
print(inventory)
