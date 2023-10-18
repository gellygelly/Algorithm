def toBinary(arr, n):
    binArr = []
    for i in arr:
        binNum = str(bin(i))
        binNum = binNum[2:]

        if len(binNum) < n:
            while len(binNum) != n:
                binNum = '0' + str(binNum)

        binArr.append(binNum)

    return binArr


def solution(n, arr1, arr2):
    binArr1 = toBinary(arr1, n)
    binArr2 = toBinary(arr2, n)

    newMap = []
    for row in range(n):
        newRow = ''
        for col in range(n):
            if binArr1[row][col] == '1' or binArr2[row][col] == '1':
                newRow += '#'
            if binArr1[row][col] == '0' and binArr2[row][col] == '0':
                newRow += ' '
        newMap.append(newRow)

    return newMap

output = solution(5,[9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
print(output)