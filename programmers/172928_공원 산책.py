def move(park, op, n, x, y):
    pos_x, pos_y = x, y
    if op == 'N':
        for nx in range(x, x - n - 1, -1):
            # 장애물 있는 칸 지나거나 맵 밖으로 벗어나면 초기값 반환
            if nx < 0 or nx >= len(park) or park[nx][y] == 'X':
                return x, y
            pos_x = nx
    elif op == 'S':
        for nx in range(x, x + n + 1, 1):
            if nx < 0 or nx >= len(park) or park[nx][y] == 'X':
                return x, y
            pos_x = nx

    elif op == 'W':
        for ny in range(y, y - n - 1, -1):
            if ny < 0 or ny >= len(park[1]) or park[x][ny] == 'X':
                return x, y
            pos_y = ny
    else:  # E
        for ny in range(y, y + n + 1, +1):
            if ny < 0 or ny >= len(park[1]) or park[x][ny] == 'X':
                return x, y
            pos_y = ny

    return pos_x, pos_y


def solution(park, routes):
    answer = []

    # 시작점 확인
    x, y = 0, 0
    for i in range(len(park)):
        if 'S' in park[i]:
            idx = park[i].find('S')
            x = i
            y = idx
            break

    for route in routes:
        op = route.split(' ')[0]  # 방향
        n = int(route.split(' ')[1])  # 거리
        print('이동 전: ', x, y)
        x, y = move(park, op, n, x, y)
        print('이동 후: ', x, y)

    answer = [x, y]

    return answer

answer = solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])
print('output:', answer)