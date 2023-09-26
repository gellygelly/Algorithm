def calculate(choice, type_a_score, type_b_score):

    # 비동의
    if choice == 1:
        type_a_score += 3
    elif choice == 2:
        type_a_score += 2
    elif choice == 3:
        type_a_score += 1
        # 동의
    elif choice == 5:
        type_b_score += 1
    elif choice == 6:
        type_b_score += 2
    elif choice == 7:
        type_b_score += 3
    else:
        pass

    print(type_a_score, type_b_score)

    return type_a_score, type_b_score


def judge(type_a, type_a_score, type_b, type_b_score):
    if type_a_score > type_b_score:
        return type_a
    elif type_a_score < type_b_score:
        return type_b
    else:
        if ord(type_a) < ord(type_b):
            return type_a
        else:
            return type_b


def solution(survey, choices):
    # type, score array
    typeArray = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    scoreArray = [0 for i in range(8)]

    # 점수 계산
    for i in range(len(choices)):
        first = survey[i][0]
        second = survey[i][1]

        firstIdx = typeArray.index(first)
        secondIdx = typeArray.index(second)

        scoreArray[firstIdx], scoreArray[secondIdx] = calculate(choices[i], scoreArray[firstIdx], scoreArray[secondIdx])

    # 성격 유형 판단
    answer = ''
    for i in range(0, 8, 2):
        answer += judge(typeArray[i], scoreArray[i], typeArray[i + 1], scoreArray[i + 1])

    print(typeArray)
    print(scoreArray)
    return answer

output = solution(["TR", "RT", "TR"],[7, 1, 3])
print(output)