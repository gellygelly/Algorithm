def sum(count):
    result = 0

    for i in range(1, count + 1):
        result += i

    return result


def solution(price, money, count):
    answer = (price * sum(count)) - money

    if answer <= 0:
        answer = 0

    return answer