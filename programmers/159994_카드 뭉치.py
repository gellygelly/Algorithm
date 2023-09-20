def solution(cards1, cards2, goal):
    useCards1 = list()
    useCards2 = list()

    for i in range(0, len(goal)):
        if goal[i] in cards1:
            useCards1.append(cards1.index(goal[i]))
        if goal[i] in cards2:
            useCards2.append(cards2.index(goal[i]))

    # 다 쓴 카드팩 검사
    for i in range(1, len(useCards1)):
        if useCards1[i] == useCards1[i - 1] + 1:
            continue
        else:
            return 'No'

    for i in range(1, len(useCards2)):
        if useCards2[i] == useCards2[i - 1] + 1:
            continue
        else:
            return 'No'

    return 'Yes'

answer = solution(["i", "drink", "water"], 	["want", "to"], ["i", "want", "to", "drink", "water"]	) # 기댓값 [1, 1]
print('output:', answer)