def solution(a, b, n):
    answer = 0

    while n >= a:
        changeBottles = (n // a) * b
        n = changeBottles + (n % a)
        answer += changeBottles

    return answer