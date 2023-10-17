from collections import deque

global graph
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y+ dy[i]
            if nx<0 or ny <0 or nx >= N or ny>=N:
                continue


if __name__=='__main__':
    N, M = map(int, input('정수 N, M 입력:').split())

    graph = []
    for i in range(N):
        graph.append(list(map(int, input('M개의 정수 입력:'))))

    print(graph)

    bfs(0, 0)


