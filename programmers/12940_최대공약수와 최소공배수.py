def solution(n, m):
    min_num = min(n, m)
    max_num = max(n, m)

    LCM = 0 # 최소공배수
    GCM = 0 # 최대공약수

    if max_num % min_num == 0:
        LCM = max_num
        GCM = min_num
    else:
        a = max_num
        b = min_num

        while b != 0:
            r = a % b
            print(r, a, b)
            a = b
            b = r

        GCM = a  # 최대공약수


        LCM = int(max_num * min_num / GCM)  # 두 수의 곱 / 최대공약수

    answer = [GCM, LCM]  # 최대공약수, 최소공배수 리턴
    return answer

answer = solution(2,5)
print('output:', answer)