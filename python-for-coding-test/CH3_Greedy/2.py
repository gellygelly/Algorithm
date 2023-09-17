# CH3 Greedy 92p <2> 큰 수의 법칙

if __name__=='__main__':
    # N: 배열의 크기
    # M: 숫자가 더해지는 횟수
    # K: 연속으로 수를 더할 수 있는 횟수
    N, M, K = map(int, input("N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000) 입력:").split())

    data = list(map(int, input("list 원소 입력(1<x<10000):").split()))


    data.sort()

    result = 0
    while M!=0:
        if M < K:
            result += M * data[N-1]
            M = 0
            break
        else:
            result += K * data[N-1]
            M = M-K

        N -= 1

    print("Output: {}".format(result))