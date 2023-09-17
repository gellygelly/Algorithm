# CH3 Greedy 99p <4> 1이 될 때까지

if __name__=='__main__':
    # N: 수, K: 나눌 수

    N, K = map(int, input("N, K 입력:").split())

    count = 0
    while(True):
        if N==1:
            break
        else:
            if N%K == 0:
                N = N/K
                count += 1
            else:
                N -= 1
                count += 1

    print('output: {}'.format(count))