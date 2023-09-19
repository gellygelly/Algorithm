
def move(op, n, x, y):
    if op == 'N':
        x -= n
    elif op == 'S':
        x += n
    elif op == 'W':
        y -= n
    else:  # E
        y += n
    return x, y

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
        op = route.split(' ')[0]
        n = int(route.split(' ')[1])
        pos_x, pos_y = move(op, n, x, y)

        # 1. 공원을 벗어나지 않는 위치인지 확인
        if pos_x >= 0 and pos_x < len(park) and pos_y >= 0 and pos_y < len(park[1]):
            # 2. 지나가는 중간 경로에 장애물이 있는지 확인
            diff_x = abs(pos_x - x)
            diff_y = abs(pos_y - y)

            check = False

            if diff_x == 0:
                for i in range(diff_y):
                    if park[pos_x][i] == 'X':
                        check = True
                        break

            if diff_y == 0:
                for j in range(diff_x):
                    if park[j][pos_y] == 'X':
                        check = True
                        break

            if check == False:
                x, y = pos_x, pos_y

    answer = [x, y]

    return answer

answer = solution( ["OXO", "XSX", "OXO"], ["S 1", "E 1", "W 1", "N 1"]) # 기댓값 [1, 1]
print('output:', answer)