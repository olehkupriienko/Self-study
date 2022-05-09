def is_palindrome(text2):
    text = [i.lower() for i in text2 if i.isalnum()]
    flag = True
    for i in range(len(text) // 2 + len(text) % 2):
        if text[i] != text[len(text)-1-i]:
            flag = False
    return flag


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))