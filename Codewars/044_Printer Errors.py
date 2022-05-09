test = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"


def printer_error(s):
    goodletters = 'abcdefghijklm'
    errors = 0
    totalletters = len(s)

    for letter in s:
        if letter not in goodletters:
            errors += 1

    return str(errors) + "/" + str(totalletters)


print(printer_error(test))
