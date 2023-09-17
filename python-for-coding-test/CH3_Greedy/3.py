# CH3 Greedy 96p <3> 숫자 카드 게임

if __name__=='__main__':
    # N: 행, M: 열

    N, M = map(int, input("1<= N, M <=100 입력:").split())

    numbers = []
    for i in range(0, N):

        data = list(map(int, input("M 개수만큼 list 원소 입력:").split()))

        numbers.append(data)

    print(numbers)

    # 1. 각 행 중 가장 작은 숫자 선별
    # 2. 선별한 숫자 중 작은 숫자가 있는 행, 열 선택

    output = 0
    for i in range(0, N):
        print(numbers[i])
        result = min(numbers[i])
        output = max(result, output)

    print("output: {}".format(output))