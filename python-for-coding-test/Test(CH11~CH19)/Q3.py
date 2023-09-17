# Q3

# start: 10:00 AM
# end: 10:11 AM

S = input('S 입력:')

# 주어진 문자열을 압축

before = S[0]
new_S = S[0] # 압축할 문자열
for i in range(1, len(S)):
    if S[i] != before:
        new_S += S[i]
        before = S[i]

count_0 = new_S.count('0')
count_1 = new_S.count('1')

if count_0 > count_1:
    result = count_1
else:
    result = count_0

print('output: ', result)