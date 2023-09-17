# Q6


def is_negative(n):
    return True

def solution(food_times, k):

    num = 0
    for i in range(0, k):
        while True:

            if len(food_times) == food_times.count(0): # 먹을 음식이 없는 경우 반복문 종료
                num = -1
                break

            if num == len(food_times):
                num = 0

            if food_times[num]>0: # 음식이 있을 경우, 1초 먹고 반복문 종료
                food_times[num] -= 1
                print('{} 초에 {} 번째 음식 섭취'.format(i, num))
                num+= 1
                break
            else: # 해당 번호 음식이 없을 경우, 다른 음식 탐색

                num += 1

    if num == len(food_times):
        num = 0
    answer = num+1

    return answer

answer = solution([3,1,2], 5)
print('output:', answer)
