test1 = ("bright aright", "ok")


def left_join(phrases: tuple) -> str:
    """
    Join strings and replace "right" to "left"
    """
    # result = ''
    # for word in phrases:
    #     word: str
    #     if 'right' in word:
    #         result += word.replace('right', 'left')
    # return result
    return ','.join(word.replace('right', 'left') for word in phrases)


print(left_join(test1))
