# Q26

if __name__=='__main__':
    N = int(input('N 입력:'))

    array = []
    for i in range(N):
        size = int(input('카드 묶음 크기 입력:'))
        array.append(size)

    sorted(array)

    cardSum = array[0]+array[1]
    result = [cardSum]
    for i in range(2, len(array)):
        cardSum = cardSum+array[i]
        result.append(cardSum)

    print(sum(result))