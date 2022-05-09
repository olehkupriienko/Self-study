print('Вас вітає програма "Шифр Цезаря".')
while True:
    print('Що ми робимо: шифруємо чи дешифруємо текст?\n'
          'Введіть вашу відповідь нижче:')
    type = input().lower()
    if type == 'шифруємо' or type == 'дешифруємо':
        print('Відповідь прийнято!')
        break
    else:
        print('Дана команда не підтримується. Повторіть ще раз.')

while True:
    print('Виберіть мову: російська чи англійська?')
    lang = input().lower()
    if lang == 'російська' or lang == 'англійська':
        print('Відповідь прийнято!')
        break
    else:
        print('Така мова не підтримується. Повторіть ще раз.')

while True:
    print('Оберіть напрямок зсуву: вліво чи вправо:')
    shift_dir = input().lower()
    if shift_dir == 'вліво' or shift_dir == 'вправо':
        print('Відповідь прийнято!')
        break
    else:
        print('Напрямок вказано неправильно. Повторіть ще раз.')

while True:
    if lang == 'російська':
        print('Оберіть крок зсуву вправо (мінімум - 1, максимум - 32).\n'
              'Якщо крок невідомо - введіть 0')
        shift_num = int(input())
        if 0 <= shift_num <= 32:
            print('Відповідь прийнята')
            break
        else:
            print('Крок обрано не правильно. Повторіть ще раз.')
    if lang == 'англійська':
        print('Оберіть крок зсуву вправо (мінімум - 1, максимум - 26).\n'
              'Якщо крок невідомо - введіть 0:')
        shift_num = int(input())
        if 0 <= shift_num <= 26:
            print('Відповідь прийнята')
            break
        else:
            print('Крок обрано не правильно. Повторіть ще раз.')

eng_alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
rus_alphabet_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
rus_alphabet_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

def cyfer_rus(): #шифруємо російську фразу
#    print('Введіть фразу на російській мові, яку потрібно зашифрувати:')
    output_phrase = ''
#    input_phrase = input()
    for i in input_phrase:
        if i in rus_alphabet_upper:
            if 0 <= rus_alphabet_upper.index(i) + shift_num <= 31:
                output_phrase += rus_alphabet_upper[rus_alphabet_upper.index(i) + shift_num]
            else:
                output_phrase += rus_alphabet_upper[rus_alphabet_upper.index(i) + shift_num - int(shift_num/abs(shift_num)) * 32]
        if i in rus_alphabet_lower:
            if 0 <= rus_alphabet_lower.index(i) + shift_num <= 31:
                output_phrase += rus_alphabet_lower[rus_alphabet_lower.index(i) + shift_num]
            else:
                output_phrase += rus_alphabet_lower[rus_alphabet_lower.index(i) + shift_num - int(shift_num/abs(shift_num)) * 32]
        if i not in rus_alphabet_upper and i not in rus_alphabet_lower:
            output_phrase += i
    return output_phrase


def cyfer_eng(): #шифруємо англійську фразу
#    print('Введіть фразу на англійській мові, яку потрібно зашифрувати:')
    output_phrase = ''
#    input_phrase = input()
    for i in input_phrase:
        if i in eng_alphabet_upper:
            if 0 <= eng_alphabet_upper.index(i) + shift_num <= 25:
                output_phrase += eng_alphabet_upper[eng_alphabet_upper.index(i) + shift_num]
            else:
                output_phrase += eng_alphabet_upper[eng_alphabet_upper.index(i) + shift_num - int(shift_num/abs(shift_num)) * 26]
        if i in eng_alphabet_lower:
            if 0 <= eng_alphabet_lower.index(i) + shift_num <= 25:
                output_phrase += eng_alphabet_lower[eng_alphabet_lower.index(i) + shift_num]
            else:
                output_phrase += eng_alphabet_lower[eng_alphabet_lower.index(i) + shift_num - int(shift_num/abs(shift_num)) * 26]
        if i not in eng_alphabet_upper and i not in eng_alphabet_lower:
            output_phrase += i
    return output_phrase

print('Введіть фразу на російській мові, яку потрібно зашифрувати:')
input_phrase = input()

if shift_num == 0:
    for shift_num in range(1, 26):
        if (type == 'шифруємо' and shift_dir == 'вправо') or (type == 'дешифруємо' and shift_dir == 'вліво'):
            if lang == 'російська':
                print(cyfer_rus())
            if lang == 'англійська':
                print(cyfer_eng())
        elif (type == 'шифруємо' and shift_dir == 'вліво') or (type == 'дешифруємо' and shift_dir == 'вправо'):
            shift_num = - shift_num
            if lang == 'російська':
                print(cyfer_rus())
            if lang == 'англійська':
                print(cyfer_eng())
else:
    if (type == 'шифруємо' and shift_dir == 'вправо') or (type == 'дешифруємо' and shift_dir == 'вліво'):
        if lang == 'російська':
            print(cyfer_rus())
        if lang == 'англійська':
            print(cyfer_eng())
    elif (type == 'шифруємо' and shift_dir == 'вліво') or (type == 'дешифруємо' and shift_dir == 'вправо'):
        shift_num = - shift_num
        if lang == 'російська':
            print(cyfer_rus())
        if lang == 'англійська':
            print(cyfer_eng())
