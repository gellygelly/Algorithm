# CH8 Dynamic Programming 226p <5> 효율적인 화폐 구성

N, M = map(int, input().split())

array = []
for i in range(N):
    array.append(int(input()))

d = [10001] * (M+1)

d[0] = 0

for i in range(N):
    for j in range(array[i], M+1):
        if d[j-array[i]] != 10001: # 해당 금액을 만드는 방법이 존재할 경우
            d[j] = min(d[j], d[j-array[i]]+1)

if d[M] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[M])