# Q4

# start: 10:31 AM
# end: 10:48 AM

N = int(input('N 입력:'))
numbers = list(map(int, input('숫자들 입력:').split()))

sum = sum(numbers)

result = 1001
for i in range(1, sum+1):
    if i in numbers: # i가 numbers list에 속한 수일 때는 다음 반복으로
        continue

    # j가 0이 될 때까지 numbers에 속한 수들을 차례로 뺌
    j = i
    for number in numbers:
        if number <= j:
            j -= number

    if j!=0: # 반복문 종료 후에도 j가 0이 아니면 i가 최솟값
        result = i
        break

print('output:', result)