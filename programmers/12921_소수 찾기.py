def solution(n):
    answer = [True for i in range(n + 1)]

    for i in range(2, int(n ** 0.5) + 1):
        if answer[i] == True:
            j = 2
            while i * j <= n:
                answer[i * j] = False
                j += 1

    answer[0] = False
    answer[1] = False

    return answer.count(True)

output = solution(11)

print(output)

