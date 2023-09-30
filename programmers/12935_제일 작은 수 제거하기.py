def solution(arr):
    minNum = min(arr)
    idx = arr.index(minNum)

    del (arr[idx])

    if len(arr) == 0:
        return [-1]
    else:
        return arr