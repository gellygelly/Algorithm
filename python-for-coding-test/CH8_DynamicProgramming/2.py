# CH8 Dynamic Programming 217p <2> 1로 만들기

x = int(input('x 입력:'))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화

d = [0] * 30001

for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우 (+1은 계산 횟수 카운트)
    d[i] = d[i-1]+1

    # 현재의 수가 2,3,5로 나누어 떨어지는 경우 (+1은 계산 횟수 카운트)
    if i%2==0:
        print('2 // d[{}] = min({}, {}) '.format(i, d[i], d[i//2]+1))
        d[i] = min(d[i], d[i//2]+1)
    if i%3==0:
        print('3 // d[{}] = min({}, {}) '.format(i, d[i], d[i//3]+1))
        d[i] = min(d[i], d[i//3]+1)
    if i%5==0:
        print('5 // d[{}] = min({}, {}) '.format(i, d[i], d[i//5]+1))
        d[i] = min(d[i], d[i//5]+1)

print('d[x]:', d[x])

