# Q1

# start: 9:33 AM
# end: 9:43 AM

N = int(input('N 입력:'))
group = list(map(int, input('list 입력:').split()))

group.sort(reverse=True)

group_count = 0
i = 0

while True:
    if i < len(group):
        if N-group[i] >= 0:
            N -= group[i]
            i += group[i]
            group_count += 1
        else:
            break
    else:
        break

print('output:', group_count)