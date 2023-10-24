def solution(nums):
    numsSet = set(nums)
    numsSet = list(numsSet)

    if len(nums) / 2 <= len(numsSet):
        return len(nums) / 2
    else:
        return len(numsSet)