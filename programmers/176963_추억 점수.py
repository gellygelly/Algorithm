def solution(name, yearning, photos):
    answer = []

    # name(key)과 yearning(value) 두 개의 list를 묶어 dict 형태로 변환
    memories = {key: int(value) for key, value in zip(name, yearning)}

    # 각 사진의 사람들을 확인하여 사진별 사람들의 그리움 점수 집계
    for photo in photos:
        sum = 0
        for person in photo:
            try:
                sum += memories[person]
            except KeyError:
                pass
        answer.append(sum)

    return answer
answer = solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
print('output:', answer)