# CH6 Binary Search 201p <3> 떡볶이 떡 만들기
# TODO: 수정 필요, M이랑 높이 H가 일치할 경우만 고려했음 (최댓값 출력해야 함)

# def cut_rice_cake(array, height):
#     sum = 0
#
#     for i in range(len(array)):
#         if height < array[i]:
#             sum += array[i] - height
#
#
#     return sum
#
# def binary_search_by_recursion(array, target, start, end):
#
#     if start>end:
#         return None
#
#     mid = (start+end)//2
#
#     # 떡을 자른 길이(result)가 target(M)보다 긴 경우 재귀
#     # 떡을 자른 길이가 M보다 짧은 경우 중단
#     result = cut_rice_cake(array, mid)
#     print(start, end, mid, result)
#
#     if result == target:
#         return mid
#     # 떡을 자른 길이(result)가 target(M)보다 긴 경우, 더 많이 잘라야 하므로 시작점 증가
#     elif result > target:
#         return binary_search_by_recursion(array, target, mid+1, end)
#     # 떡을 자른 길이가 target보다 짧은 경우, 덜 잘라야 하므로 끝점 감소
#     else:
#         return binary_search_by_recursion(array, target, start, end-1)
#
# N, M = map(int, input('N, M 입력:').split())
# array = list(map(int, input('N개의 정수 입력:').split()))
#
# start = 0
# end = max(array)
#
# height = binary_search_by_recursion(array, M, start, end)
#
# print('output:', height)

N, M = map(int, input('N, M 입력:').split(' '))
array = list(map(int, input('N개의 정수 입력:').split()))

start = 0
end = max(array)

def cut_rice_cake(array, height):
    sum = 0
    for i in array:
        if i >= height:
           sum += i-height

    return sum

result = 0

while start<=end:
    mid = (start+end)//2

    sum = cut_rice_cake(array, mid)

    # 절단기 길이 증가 -> 잘리는 떡의 길이 감소
    # 절단기 길이 감소 -> 잘리는 떡의 길이 증가
    if sum == M:
        result = mid
        break
    elif sum > M: # 잘린 떡 길이의 합이 손님이 요청한 길이(M)보다 길 경우
        result = start
        start = mid + 1 # 절단기 길이를 늘려줌
    else: # 잘린 떡 길이의 합이 손님이 요청한 길이(M) 보다 짧을 경우
        end = mid - 1 # 절단기 길이를 줄임


print('output:', result)
