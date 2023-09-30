def cal(num):
    result = []

    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)

    if len(result) % 2 == 0:
        return num
    else:
        return -num
    return num


def solution(left, right):
    answer = 0

    for i in range(left, right + 1, 1):
        answer += cal(i)

    return answer