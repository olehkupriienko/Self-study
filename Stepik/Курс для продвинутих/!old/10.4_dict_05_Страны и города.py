n = int(input())

country_and_city = {}

for _ in range(n):
    country, *cities = input().split()
    country_and_city[country] = cities

m = int(input())
cities_to_find = [input() for _ in range(m)]

for i in range(m):
    for country in country_and_city:
        if cities_to_find[i] in country_and_city[country]:
            print(country)
