def solution(s):
    charList = list(s)
    charList = sorted(charList, reverse=True)

    answer = ''.join(charList)

    return answer