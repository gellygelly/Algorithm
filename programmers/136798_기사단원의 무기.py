def solution(number, limit, power):
    answer = [1]

    for i in range(2, number + 1):
        count = 2  # 1, 자기 자신

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 1
                if j * j != i:
                    count += 1

            if count > limit:
                count = power
                break

        answer.append(count)

    return sum(answer)