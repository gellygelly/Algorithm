def solution(s):
    s = s.upper()

    p = s.count('P')
    y = s.count('Y')

    if p == y:
        return True
    else:
        return False