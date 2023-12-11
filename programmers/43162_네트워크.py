def dfs(computers, i, visited):
    if visited[i]:
        return False

    visited[i] = 1

    for j in range(len(computers)):
        if computers[i][j] == 1:
            dfs(computers, j, visited)

    return True

def solution(n, computers):
    answer = 0
    visited = [0] * n

    for i in range(n):
        if visited[i] == 0:
            if dfs(computers, i, visited):
                answer += 1

    return answer