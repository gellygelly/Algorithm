from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    termsInfo = dict()  # Key-약관, Value: 유효 기간(달)으로 이루어진 dict 생성

    for term in terms:
        termsInfo[term.split(' ')[0]] = int(term.split(' ')[1])

    answer = []

    for idx, privacy in enumerate(privacies):
        # 각 개인정보를 date와 term으로 split
        date = privacies[idx].split(' ')[0]
        term = privacies[idx].split(' ')[1]

        # 개인정보의 유효 만료일 계산
        date = datetime.strptime(date, '%Y.%m.%d') + relativedelta(months=termsInfo[term])

        # today - 유효 만료일 계산
        result = datetime.strptime(today, '%Y.%m.%d') - date
        result = str(result).split(' ')[0]

        if result == '0:00:00':
            answer.append(idx + 1)
        elif int(result) > 0:
            answer.append(idx + 1)  # idx가 1부터 시작함

    return answer

answer = solution("2022.05.19", ["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"] )
print('output:', answer)
print('--')
answer = solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
print('output:', answer)