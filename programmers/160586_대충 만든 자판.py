
def solution(keymap, targets):
    answer = []
    for target in targets:
        result = 0
        emptyCheck = False
        for string in target:
            idxList = []
            for key in keymap:
                if string in key:
                    idxList.append(key.find(string)+1)
            try:
                idx = min(idxList)
                result += idx
            except ValueError:
                emptyCheck = True
        if emptyCheck:
            answer.append(-1)
        else:
            answer.append(result)
    print(answer)
    return answer

output = solution(["BC"], ["AC", "BC"]) # 기댓값 [-1, 3]
print(output)