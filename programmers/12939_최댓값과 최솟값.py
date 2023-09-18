def solution(s):
    string = s.split(' ')
    string = list(map(int, string))

    max_s = max(string)
    min_s = min(string)

    answer = str(min_s) + ' ' + str(max_s)

    return answer