def solution(sizes):
    widthSizes = []
    heightSizes = []

    for size in sizes:

        if size[0] >= size[1]:
            widthSizes.append(size[1])
            heightSizes.append(size[0])
        else:
            widthSizes.append(size[0])
            heightSizes.append(size[1])

    w = max(widthSizes)
    h = max(heightSizes)

    return w * h

output = solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
print(output)