# CH4 Implementation 115p <2> 왕실의 나이트

if __name__=='__main__':

    move = input('나이트의 좌표(열, 행):')

    y = ord(move[0])-96
    x = int(move[1])

    print('x: {}, y: {}'.format(x, y))

    cases = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    count = 0
    for case in cases:
        temp_x, temp_y = x+case[0], y+case[1]

        if temp_x <= 8 and temp_x >=1 and temp_y <=8 and temp_y >=1:
            print(case, temp_x, temp_y)
            count+=1

    print('count: {}'.format(count))