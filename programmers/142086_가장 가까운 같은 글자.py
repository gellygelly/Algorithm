def solution(string):
    answer = [-1]

    for idx in range(1, len(string)):
        adjacentCharIdx = string[:idx].rfind(string[idx])
        if adjacentCharIdx != -1:
            answer.append(idx - adjacentCharIdx)
        else:
            answer.append(adjacentCharIdx)
    return answer