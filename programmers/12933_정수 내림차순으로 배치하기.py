def solution(n):
    numList = list(map(int, str(n)))
    result = sorted(numList, reverse=True)

    answer = ''
    for i in result:
        answer += str(i)

    return int(answer)

output = solution(118372)
print(output)