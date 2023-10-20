# CH8 Dynamic Programming 220p <3> 개미 전사

n = int(input('n 입력:'))
array = list(map(int, input('N개의 정수 입력:').split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(d[0], array[1])

# {1, 3, 1, 5}
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])