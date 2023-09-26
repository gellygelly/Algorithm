def solution(n, m, section):
    start = section[0]
    end = start + m - 1

    count = 1
    for wall in section:
        if end < wall:
            start = wall
            end = start + m - 1
            count += 1

    return count