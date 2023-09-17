# Q5

# start: 1:40 PM
# end: 2:00 PM

# 볼링공 개수 N, 공의 최대 무게 M
N, M = map(int, input('N, M 입력:').split())
K = list(map(int, input('list 원소 입력:').split()))

result = N * (N-1) / 2

KSet = set(K)
for i in KSet:
    if K.count(i)>1:
        result -= K.count(i)*(K.count(i)-1)/2

print('output:', int(result))