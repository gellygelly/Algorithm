def solution(a, b):
    answer = 0

    for idx in range(len(a)):
        sum = a[idx] * b[idx]
        answer += sum

    return answer