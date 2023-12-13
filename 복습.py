from collections import deque


def bfs(skills, i, visited):
    queue = deque([i])
    visited[i] = 1

    while queue:
        v = queue.popleft()

        for i in range(len(skills)):
            if skills[i][0] + 1 == i:
                if visited[skills[i][1] - 1] == 0:
                    queue.append(i)
                    visited[skills[i][1] - 1] = 1
                    visited[skills[i][0] - 1] += visited[skills[i][1] - 1]

def solution(total_sp, skills):
    visited = [0] * len(skills)

    bfs(skills, 0, visited)

    print(visited)

    return visited

output = solution(121, [[1,2],[1,3], [3,6], [3,4], [3,5]])