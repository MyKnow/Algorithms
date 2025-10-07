# * 정리
# - 각 유저는 한 번에 한 명의 유저를 신고할 수 있음
#   - 신고 횟수에 제한 없음.
#   - 한 유저를 여러 번 신고 가능하나, 동일한 유저에 대한 신고 횟수는 1회로 처리됨.
# - k번 이상 신고된 유저는 게시판 이용 정지, 신고한 유저들에게 메일 알림 전송.
#   - 모든 내용 취합 후 마지막에 한꺼번에 이용 정지 및 정지 메일 발송 처리
    
# * 입력
# - id_list: 게시판 이용자 아이디 리스트(알파벳 소문자 only, 중복 없음)
# - report: "이용자id 신고한id" 형태의 문자열 리스트(공백 하나로 구분, 알파벳 소문자 only, 자기 자신 신고 없음)
# - k: 정지 기준이 되는 신고 횟수
#
# * 출력
# - 입력 1번 순서대로, 각 유저가 받은 결과 메일 수 리스트

from collections import defaultdict

def solution(id_list, report, k):
    # 1. 이용자 -> 횟수, 피신고자 -> 이용자 사전을 각각 만든다.
    # 중복 신고는 무시되어야 하기에 피신고자 사전의 값 자료형은 set으로 지정한다.
    user_dict = defaultdict(int)
    reported_dict = defaultdict(set)
    
    # 2. report를 순회하며 피신고자 사전을 업데이트한다.
    for r in report:
        # 공백을 기준으로 이용자와 피신고자를 구분하여 저장한다.
        user, reported = r.split(" ")
        reported_dict[reported].add(user)
        
    # 3. reported_dict를 순회하며, 값이 k 이상인 피신고자를 신고한 이용자는 user_dict의 값을 증가시킨다.
    for key, value in reported_dict.items():
        if len(value) >= k:
            for user in value:
                user_dict[user] += 1
        
    # 4. id_list 순서대로 값을 반환한다.
    return [user_dict[user] for user in id_list]