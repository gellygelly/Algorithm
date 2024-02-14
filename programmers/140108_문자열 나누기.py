def solution(s):
    answer = 0

    index = 1
    x_count = 1
    other_count = 0

    if len(s) == 1:
        return 1

    while True:
        if s[0] == s[index]:
            x_count += 1
        else:
            other_count += 1

        index += 1

        if x_count == other_count:
            s = s[index:]
            answer += 1
            index = 1
            x_count = 1
            other_count = 0

        if s == "":
            break

        if index == len(s) or len(s) == 1:
            answer += 1
            break

    return answer

output = solution("banana")
print(output)