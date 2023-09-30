def solution(s):
    answer = ''
    count = 0
    for char in s:
        if char != ' ':
            if count % 2 == 0:
                answer += char.upper()
            else:
                answer += char.lower()
            count += 1
        else:
            answer += ' '
            count = 0

    return answer