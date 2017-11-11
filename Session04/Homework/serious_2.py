prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
}

stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15
    }
goods = ["banana", "apple", "orange", "pear"]
total = 0
for i in range(len(goods)):
    print(goods[i], ":  ", stock[goods[i]])
    print("Price: ", prices[goods[i]])
    total += prices[goods[i]] * stock[goods[i]]
print("The total money i got: ", total)
