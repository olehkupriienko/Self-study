test = "three occurrences"
test2 = 'r'


def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    if text.count(symbol) >= 2:
        first_index = text.find(symbol)
        print(first_index)
        last_index = text.find(symbol, first_index+1)
        return last_index
    else:
        return None


print(second_index(test, test2))
