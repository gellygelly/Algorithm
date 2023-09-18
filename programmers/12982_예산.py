# 조건 #
# 1. 최대한 많은 부서의 물품을 구매해 줄 수 있도록 할 것
# 2. 각 부서가 신청한 금액만큼은 모두 지원해줄 것

def solution(d, budget):
    result = 0
    d = sorted(d)

    idx = 0
    while budget > 0 and idx < len(d):
        budget -= d[idx]
        idx += 1
        result += 1

    if budget < 0 :
        result -= 1

    return result

answer = solution([1,3,2,5,4],9)
print('output:', answer)