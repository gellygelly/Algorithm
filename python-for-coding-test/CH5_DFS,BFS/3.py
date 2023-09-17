# CH5 DFS,BFS 149p <3> 음료수 얼려 먹기

def dfs(x, y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

        return True
    else:
        return False

if __name__=='__main__':
    global N, M
    N, M = map(int, input("N, M 입력:").split())

    global graph
    graph = []
    for i in range(0, N):
        row = list(map(int, input("list 원소 입력(1<x<10000):").split()))
        graph.append(row)

    print(graph)

    count = 0
    for x in range(N):
        for y in range(M):
            if dfs(x, y):
                count+=1

    print('output: {}'.format(count))



