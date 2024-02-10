def solution(N, stages):
    answer = []

    users = len(stages)
    for i in range(1, N + 1):
        fail_count = stages.count(i)

        if users != 0:
            answer.append((fail_count / users, i))
            users -= fail_count
        else:
            answer.append((0, i))

    answer = sorted(answer, reverse=True, key=lambda x: x[0])
    answer = [x[1] for x in answer]

    return answer