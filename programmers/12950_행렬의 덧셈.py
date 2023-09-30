def solution(arr1, arr2):
    answer = []

    for row in range(len(arr1)):
        result = []
        for col in range(len(arr1[row])):
            sum = arr1[row][col] + arr2[row][col]
            result.append(sum)
        answer.append(result)

    return answer