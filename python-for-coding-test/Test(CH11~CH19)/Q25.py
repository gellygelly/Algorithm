# Q25

if __name__=='__main__':
    N = int(input('스테이지의 개수 N 입력:'))
    stages = list(map(int, input('사용자들이 현재 멈춰있는 스테이지 번호 배열: ').split()))

    print(stages)
    fail = []
    sum = 0
    for i in range(1, N+1):
        count = stages.count(i)
        print(i, count,  count/(len(stages)-sum))
        fail.append([i, count/(len(stages)-sum)])
        sum += count

    fail = sorted(fail, key=lambda x: x[1], reverse=True)

    print([i[0] for i in fail])



    # 실패율이 높은 스테이지 번호부터 return