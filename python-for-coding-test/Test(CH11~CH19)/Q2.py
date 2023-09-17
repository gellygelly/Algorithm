# Q2

# start: 9:43 AM
# end: 9:56 AM

S = input('S 입력:')

# 0이 아니라면, 모두 곱하는 것이 이득

# 0 2 9 8 4
result = 0
for i in range(0, len(S)):
    if int(S[i]) == 0 or result == 0:
        result += int(S[i])
    else:
        if i == 0:
            result = int(S[i])
        else:
            result *= int(S[i])

print('output:', result)