# CH5 4번 미로 탈출

# bfs 소스코드 구현
from collections import deque


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = x+dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx <0 or nx >=n or ny <0 or ny >=m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny]==0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((x, y))

    return graph[n-1][m-1]


global graph
if __name__=='__main__':
    N, M = map(int, input('정수 N, M 입력:').split())

    graph = []
    for i in range(N):
        graph.append(list(map(int, input('M개의 정수 입력:'))))

    print(graph)

    print(bfs(0, 0))