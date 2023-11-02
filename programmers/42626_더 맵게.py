import heapq


def solution(scoville, K):
    count = 0

    hq = []

    for i in range(len(scoville)):
        heapq.heappush(hq, scoville[i])

    while hq[0] < K:
        try:
            first = heapq.heappop(hq)
            second = heapq.heappop(hq)

            newScore = first + (second * 2)

            heapq.heappush(hq, newScore)

            count += 1
        except:
            count = -1
            break

    return count