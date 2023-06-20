numbers_0 = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}
numbers = {
    1: ".,?!:",
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ",
    0: " "
}

phrase = input().upper()

result = ''

for letter in phrase:
    for key in numbers.keys():
        if letter in numbers.get(key):
            result += str(key) * (numbers.get(key).index(letter) + 1)

for letter in phrase:
    for key, value in numbers.items():
        if letter in value:
            result += str(key) * (numbers.get(key).index(letter) + 1)

print(result)
