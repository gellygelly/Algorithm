def solution(phone_book):
    answer = True

    phone_book = sorted(phone_book, key=lambda x: (x, len(x)))
    samelength = False

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
            break

    return answer