test1 = "... --- -- .   - . -..- -"
test2 = ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"

def morse_decoder(code):
    # replace this for solution

    MORSE = {
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z",
        "-----": "0",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
    }

    sentence = code.split('   ')
    decode = []
    for word in sentence:
        res = []
        for letter in word.split(' '):
            res.append(MORSE.get(letter))
        decode.append(res)
    line = ' '.join(''.join(str(i) for i in item) for item in decode).capitalize()
    return line


print(morse_decoder(test1))
print(morse_decoder(test2))
