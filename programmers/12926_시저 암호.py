def solution(s, n):
    answer = ''

    for char in s:
        if char == ' ':
            answer += ' '
        else:
            asciiNum = ord(char) + n
            if char.isupper():
                if asciiNum > 90:
                    answer += chr(asciiNum - 26)
                else:
                    answer += chr(asciiNum)
            else:
                if asciiNum > 122:
                    answer += chr(asciiNum - 26)
                else:
                    answer += chr(asciiNum)

    return answer