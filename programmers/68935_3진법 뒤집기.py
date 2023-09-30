def base10to3(num):
    result = []

    while num > 0:
        remain = num % 3
        num = num // 3
        result.append(str(remain))

    result = ''.join(result)

    return result

def base3to10(num):
    result = 0

    for i in range(0, len(num)):
        result += int(num[i]) * (3 ** (len(num) - 1 - i))

    return result


def solution(n):
    n = base10to3(n)
    answer = base3to10(n)

    return answer