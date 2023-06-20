# sentence = input()
sentence = 'London is the capital of Great Britain. More than six million people live in London. London lies on both ' \
       'banks of the river Thames. It is the largest city in Europe and one of the largest cities in the world. ' \
       'London is not only the capital of the country, it is also a very big port, one of the greatest commercial ' \
       'centres in the world, a university city, and the seat of the government of Great Britain! '

formated_sentence = ''
for i in sentence.lower():
    if i.isalpha() or i.isspace():
        formated_sentence += i

result = {}
for word in formated_sentence.split():
    result[word] = result.get(word, 0) + 1

minimum = min(result.values())

result2 = []
for key, value in result.items():
    if value == minimum:
        result2.append(key)

print(sorted(result2)[0])
