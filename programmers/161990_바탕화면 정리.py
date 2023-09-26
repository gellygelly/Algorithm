def solution(wallpaper):
    pos_x = []
    pos_y = []
    for row in range(0, len(wallpaper)):
        for col in range(0, len(wallpaper[row])):
            if wallpaper[row][col] == '#':
                pos_x.append(row)
                pos_y.append(col)

    # 드래그 시작점
    lux = min(pos_x)
    luy = min(pos_y)

    # 드래그 끝점
    rdx = max(pos_x) + 1
    rdy = max(pos_y) + 1

    answer = [lux, luy, rdx, rdy]
    return answer