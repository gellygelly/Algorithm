# CH6 Binary Search 197p <2> 부품 찾기

N = int(input('N 입력:'))
comp_list = list(map(int, input('N개의 정수 입력:').split()))

M = int(input('M 입력:'))
demand_list = list(map(int, input('M개의 정수 입력:').split()))

check = []
for comp in demand_list:
    if comp in comp_list:
        check.append('yes')
    else:
        check.append('no')

print('output:', check)