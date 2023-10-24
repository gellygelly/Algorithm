def solution(food):
    answer = ''

    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            mid = int(len(answer) / 2)
            answer = answer[:mid] + str(i) + str(i) + answer[mid:]

    answer = answer[:mid + 1] + '0' + answer[mid + 1:]

    return answer

output = solution([1, 3, 4, 6])
print(output)