def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0]-1
        j = command[1]
        k = command[2]-1
        newArray = array[i:j]
        newArray = sorted(newArray)
        answer.append(newArray[k])

    return answer

output = solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])
print(output)