import itertools
import math


def isPrime(num):
    if num == 1 or num == 0:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    answer = set()

    for i in range(1, len(numbers) + 1):
        nPr = itertools.permutations(numbers, i)
        nPr = list(nPr)
        for j in range(len(nPr)):
            num = ''.join(list(nPr[j]))
            if isPrime(int(num)):
                answer.add(int(num))

    return len(answer)