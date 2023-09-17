# CH4 Implementation 111p <예제 4-1> 상하좌우

if __name__=='__main__':

    # 첫째 줄 - N: 공간의 크기 / 둘째 줄 - 이동 계획서

    N = int(input("N(공간의 크기) 입력:"))
    plan = list(map(str, input("이동 계획 입력:").split()))

    x, y = 1, 1
    for move in plan:
        temp_x, temp_y = x, y
        if move == 'L':
            temp_y -= 1
        elif move == 'R':
            temp_y += 1
        elif move == 'U':
            temp_x -= 1
        else: # D
            temp_x += 1

        if temp_x > 0 and temp_x <= N:
            x = temp_x

        if temp_y > 0 and temp_y <= N:
            y = temp_y

        print('x:', x, 'y:', y)


    print("x: {}, y: {}".format(x,y))