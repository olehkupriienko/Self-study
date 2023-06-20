test = "Hello World hello"


def checkio(words: str) -> bool:
    flag = False
    counter = 0
    for i in words.split(' '):
        if i.isalpha():
            counter +=1
            if counter >= 3:
                flag = True
                break
        else:
            counter = 0
    return flag



