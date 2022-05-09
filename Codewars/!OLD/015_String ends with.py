
def solution(string, ending):
    return ending == string[len(string)-len(ending):]


def solution2(string, ending):
    return string.endswith(ending)



print(solution2('abcde', ''))
