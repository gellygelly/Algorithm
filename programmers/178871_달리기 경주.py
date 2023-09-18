# ＊

def solution(players, callings):
    # 해시 사용 필요 -> 리스트로 구현 시 제한사항 때문에 시간 초과되는 테스트 케이스 존재
    rankings = {players: int(idx) for idx, players in enumerate(players)}

    # 1. callings dict의 인덱스를 순차적으로 돌면서
    # 2. 해당 선수의 이름이 불릴 때마다 해당 선수의 인덱스와 바로 앞 선수 인덱스 교환

    for name in callings:
        idx = rankings[name]

        rankings[name] -= 1
        rankings[players[idx - 1]] += 1

        players[idx], players[idx - 1] = players[idx - 1], name

    return players


answer = solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"])
print('output:', answer)