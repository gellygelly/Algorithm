# CH4 Implementation 118p <3> 게임 개발

def turn(direction):
    if direction == 0:
        direction = 3
    else:
        direction -= 1

    return direction

if __name__=='__main__':

    N, M = map(int, input('정수 N, M 입력:').split())
    A, B, direction = map(int, input('캐릭터의 위치 (A, B)와 방향 입력:').split())

    gameMap = []
    for i in range(0, N):
        data = list(map(int, input("M 개수만큼 list 원소 입력:").split()))
        gameMap.append(data)

    gameMap[A][B] = 2
    direction = 0  # 북쪽 바라보고 시작

    count = 1 # 현재 있는 자리 포함
    turn_count = 0

    # 방향 설정
    while True:

        dx, dy = 0, 0
        direction = turn(direction)

        # 1. 왼쪽 방향으로 이동
        if direction == 0: # 북쪽
            dx, dy = A-1, B+0

        elif direction == 1: # 동쪽
            dx, dy =  A+0, B-1

        elif direction == 2: # 남쪽
            dx, dy = A+1, B+0
        else: # 서쪽
            dx, dy = A+0, B+1

        # 2-1. 육지일 경우 이동
        if gameMap[dx][dy] == 0:
            turn_count = 0
            count += 1
            gameMap[dx][dy] = 1 # 가본 칸 1로 표시
            A, B = dx, dy # 이동
            print('A: {}, B: {}'.format(A, B))
            continue

        # 2-2. 가본 칸일 경우 회전만
        elif gameMap[dx][dy] == 1:
            direction = turn(direction)
            turn_count += 1
            continue

        # 3. 네 방향 모두 가본 칸일 때 뒤로 이동
        if turn_count == 4:
            if direction == 0:  # 북쪽
                dx, dy = A + 0, B + 1

            elif direction == 1:  # 동쪽
                dx, dy = A - 1, B + 0

            elif direction == 2:  # 남쪽
                dx, dy = A + 0, B - 1

            else:  # 서쪽
                dx, dy = A + 1, B + 0

            if gameMap[dx][dy] != 1: # 바다가 아니면 한 칸 뒤로 이동, 대신 카운트 X
                A, B = dx, dy
                print('A: {}, B: {}'.format(A,B))
            else: # 바다면 종료
                break

        print(gameMap)
    print('count: {}'.format(count))