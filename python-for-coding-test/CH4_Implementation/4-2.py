# CH4 Implementation 113p <예제 4-2> 시각

if __name__=='__main__':

    N = int(input('정수 N 입력:'))

    count = 0
    for hour in range(0, N+1):
        for minute in range(0, 60):
            for second in range(0, 60):
                time = str(hour)+str(minute)+str(second)

                if time.__contains__('3'):
                    count += 1

    print('count: {}'.format(count))