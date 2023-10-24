import heapq

def solution(k, score):
    answer = []

    hq = []
    for i in range(len(score)):
        if i + 1 > k:
            if hq[0] < score[i]:
                heapq.heappush(hq, score[i])
                heapq.heappop(hq)
        else:
            heapq.heappush(hq, score[i])

        answer.append(hq[0])

    return answer