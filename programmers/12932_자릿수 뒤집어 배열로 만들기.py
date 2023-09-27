def solution(n):
    answer = []

    for i in range(len(str(n)) - 1, -1, -1):
        num = str(n)[i]
        answer.append(int(num))

    return answer