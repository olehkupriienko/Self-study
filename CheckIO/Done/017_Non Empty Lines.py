test = '''
Lorem ipsum dolor sit amet,

consectetur adipiscing elit
Nam odio nisi, aliquam
            '''


def non_empty_lines(text: str) -> int:
    # your code here
    # res = text.split('\n')
    res = text.splitlines()
    counter = 0
    for line in res:
        # if not line.isspace() or line != '':
        if line.isspace() or line == '':
            counter += 1
    return len(res)-counter


print(non_empty_lines(test))
