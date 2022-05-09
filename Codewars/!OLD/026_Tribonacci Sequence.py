test = [1, 1, 1]


def tribonacci(signature, n):
    result = signature
    [result.append(result[-3] + result[-2] + result[-1]) for i in range(len(signature) + 1, n + 1)]
    return result[:n]


print(tribonacci(test, 10))