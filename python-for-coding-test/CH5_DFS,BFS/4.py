# CH5 DFS,BFS 152p <4> 미로 탈출

from collections import deque

N, M = map(int, input("N, M 입력:").split())

graph = []

for i in range(N):
    graph.append(list(map(int, input('list 원소 입력:'))))

print(graph)

dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y]+1


    return graph[N-1][M-1]

print('output: ', bfs(0, 0))

