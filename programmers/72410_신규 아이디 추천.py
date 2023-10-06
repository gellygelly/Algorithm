def recommend(new_id):
    endCheck = False
    # 1
    new_id = new_id.lower()

    for i in range(len(new_id)):
        # 2
        if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] in ['-', '_', '.']:
            # 3
            if new_id[i] == '.':
                if endCheck == True:
                    new_id = new_id[:i] + ' ' + new_id[i + 1:]
                else:
                    endCheck = True
            else:
                endCheck = False
        else:
            new_id = new_id.replace(new_id[i], ' ')

    new_id = new_id.replace(' ', '')

    # 4
    try:
        if new_id[0] == '.':
            new_id = new_id[1:]

        if new_id[-1] == '.':
            new_id = new_id[:-1]
    except IndexError:
        new_id = 'a'

    # 5
    if len(new_id) == 0:
        new_id = 'a'

    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]

    return new_id


def solution(new_id):
    answer = recommend(new_id)

    return answer

output = solution("...!@BaT#*..y.abcdefghijklm")
print(output)
