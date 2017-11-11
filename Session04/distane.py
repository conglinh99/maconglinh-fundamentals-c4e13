from haversine import haversine


cities = [
{
    'name': "Hà Nội",
    'lat': 21.0277644,
    'lng': 105.83415979999995
},
{
    'name': "Đà Nẵng",
    'lat': 16.0544068,
    'lng': 108.20216670000002
},
{
    'name': "Hồ Chí Minh",
    'lat': 10.8230989,
    'lng': 106.6296638
},
{
    'name': "Singapore",
    'lat': 1.352083,
    'lng': 103.81983600000001
}
]

n = len(cities)

for i in range(0, n-1):
    for j in range(i + 1, n):
        city1 = cities[i]
        city2 = cities[j]
        # city3 = hochiminh
        # city4 = singapore
        # list_of_city = [hanoi, danang, hochiminh, city4]
        cord1 = [city1['lat'], city1['lng']]
        cord2 = [city2['lat'], city2['lng']]

        distane = haversine(cord1, cord2)
        print("The distane from {0} to {1} is {2} km"
        .format(city1['name'], city2['name'], distane))
