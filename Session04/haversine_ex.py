from haversine import haversine
hanoi = [21, 105]
danang = [16, 108]
distane = haversine(hanoi, danang)
print(distane)
