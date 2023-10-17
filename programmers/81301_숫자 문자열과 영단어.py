def solution(string):
    answer = ''

    enWords = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for word in enWords:
        if string.find(word) != -1:
            string = string.replace(word, str(enWords.index(word)))

    answer = int(string)

    return answer