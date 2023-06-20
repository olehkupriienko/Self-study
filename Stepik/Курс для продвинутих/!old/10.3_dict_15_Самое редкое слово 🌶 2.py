# sentence = input()
sentence = 'London is the capital of Great Britain. More than six million people live in London. London lies on both ' \
       'banks of the river Thames. It is the largest city in Europe and one of the largest cities in the world. ' \
       'London is not only the capital of the country, it is also a very big port, one of the greatest commercial ' \
       'centres in the world, a university city, and the seat of the government of Great Britain! '

formated_sentence = [word.strip('.,!?:;-') for word in sentence.lower().split()]

temp_dict = {}
for word in formated_sentence:
    temp_dict[word] = temp_dict.get(word, 0) + 1


print(temp_dict)
key_list_of_minimum_value = [key for key, value in temp_dict.items() if value == min(temp_dict.values())]

print(sorted(key_list_of_minimum_value)[0])
