def solution(k, m, score):
    maxPrice = 0
    score.sort()

    start = len(score) - m
    end = len(score)

    while end >= m:
        appleBox = score[start:end]

        maxPrice += appleBox[0] * m
        end = start
        start -= m

    return maxPrice