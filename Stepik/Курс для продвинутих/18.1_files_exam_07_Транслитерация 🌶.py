transliteration_dict = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
    }

with open('18.1_files_exam_07_cyrillic.txt', 'r', encoding='utf-8') as input_file, open(
        '18.1_files_exam_07_transliteration.txt', 'w', encoding='utf-8') as output_file:
    text = input_file.read()

new_text = ''
for letter in text:
    if letter.lower() in transliteration_dict:
        if letter == letter.lower():
            new_text += transliteration_dict[letter]
        elif letter == letter.upper():
            new_text += transliteration_dict[letter.lower()].title()
    else:
        new_text += letter

print(new_text)