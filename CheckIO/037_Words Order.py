def words_order(text: str, words: list) -> bool:
    text = [word for word in text.split()]
    indexes = []
    for word in words:
        if word not in text:
            return False
        else:
            indexes.append(text.index(word))
    return all(indexes[i] < indexes[i + 1] for i in range(len(indexes) - 1))


print(words_order("hi world im here", ["world", "here"]) == True)
print(words_order("hi world im here", ["here", "world"]) == False)
print(words_order("hi world im here", ["world"]) == True)
print(words_order("hi world im here", ["world", "here", "hi"]) == False)
print(words_order("hi world im here", ["world", "im", "here"]) == True)
print(words_order("hi world im here", ["world", "hi", "here"]) == False)
print(words_order("hi world im here", ["world", "world"]) == False)
print(words_order("hi world im here", ["country", "world"]) == False)
print(words_order("hi world im here", ["wo", "rld"]) == False)
print(words_order("", ["world", "here"]) == False)
print(words_order("london in the capital of great britain", ["london"]) == True)
