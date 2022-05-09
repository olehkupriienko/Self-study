# объявление функции
def is_pangram(text):
    alfabet = 'qwertyuiopasdfghjklzxcvbnm'
    for i in alfabet:
        if i not in text.lower():
            return False
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))