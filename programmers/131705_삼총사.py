def solution(numbers):
    answer = 0

    for i in range(len(numbers) - 2):
        for j in range(i + 1, len(numbers) - 1):
            for k in range(j + 1, len(numbers)):
                sum = numbers[i] + numbers[j] + numbers[k]
                if sum == 0:
                    answer += 1

    return answer