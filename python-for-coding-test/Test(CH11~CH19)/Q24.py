# Q24

if __name__=='__main__':
    N = int(input('N 입력:'))
    distances = map(int, input('N채의 집 거리:').split())

    distances = sorted(distances)
    print(distances)

    mid = len(distances)//2

    print(distances[mid-1])