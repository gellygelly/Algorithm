def check(num):
    temp = 2

    while temp < (num // 2):
        if num % temp == 0:
            return False
        else:
            temp += 1

    return True

def solution(nums):
    result = 0

    nums.sort()
    arr = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                    if check(nums[i] + nums[j] + nums[k]):
                        result += 1

    return result