def solution(babbling):
    answer = 0

    word = ["aya", "ye", "woo", "ma"]

    for i in range(len(babbling)):
        for j in range(len(word)):
            count = babbling[i].count(word[j])
            if count == 1:
                babbling[i] = babbling[i].replace(word[j], "1")

            elif count > 1:
                if word[j] * 2 not in babbling[i]:
                    babbling[i] = babbling[i].replace(word[j], "1")

        temp = babbling[i].replace("1", "")
        if temp == "":
            answer += 1
            babbling[i] == ""

    return answer