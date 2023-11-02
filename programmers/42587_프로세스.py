from collections import deque


def solution(priorities, location):
    q = deque([])

    for i in range(len(priorities)):
        q.append((priorities[i], i))

    count = 0
    while len(q) != 0:
        if max(q)[0] == q[0][0]:
            priority, index = q.popleft()
            count += 1
            if index == location:
                break
        else:
            priority, index = q.popleft()
            q.append((priority, index))

    return count