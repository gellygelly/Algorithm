import collections

def solution(clothes):
    answer = 1

    d = dict()

    for cloth in clothes:
        try:
            d[cloth[1]] += 1
        except KeyError:
            d[cloth[1]] = 1

    for k in d.keys():
        print(d[k])
        answer *= (d[k] + 1)

    return answer - 1