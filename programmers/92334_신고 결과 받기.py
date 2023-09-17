# 1. 한 번의 한 명 유저 신고 가능
# 2. 동일의 유저에 대한 신고 횟수는 1회로 처리
# 3. k번 이상 신고된 유저는 게시판 정지 -> 메일 발송(마지막에)

def solution(id_list, report, k):
    # 1. 중복된 신고 결과 제거
    report = list(set(report))

    # 2. 유저별 신고당한 횟수 및 각 유저가 신고한 ID 리스트로 정리
    result_list = [0 for i in range(len(id_list))]  # 유저별 신고당한 횟수
    report_list = [[] for i in range(len(id_list))]  # 유저가 신고한 ID 목록

    for i in report:
        user_id = i.split(' ')[0]  # 이용자 id
        reported_id = i.split(' ')[1]  # 신고한 id

        report_list[id_list.index(user_id)].append(reported_id)
        result_list[id_list.index(reported_id)] += 1

    answer = [0 for i in range(len(id_list))]  # 유저가 받을 결과 메일 수

    # 3. 정지된 유저 판별 및 각 유저가 받을 결과 메일 수 집계
    for i in range(0, len(result_list)):
        if result_list[i] >= k:  # 정지 요건을 만족하면
            reported_id = id_list[i]  # 신고당한 id

            for j in range(0, len(report_list)):
                if reported_id in report_list[j]:
                    answer[j] +=1

    return answer

answer = solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
print('output:', answer)