# 실패율: 스테이지 도달, 클리어하지 못한 수 / 스테이지 도달한 수

# 입력
# N: 전체 스테이지 개수
# stages: 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호 배열

# 출력
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열

from collections import Counter

def solution(N, stages):
    # 각 스테이지별 카운터 생성
    stage_counter = Counter(stages)
    
    # 실패율을 계산할 남은 사용자 수
    total_players = len(stages)
    
    result = []
    for stage in range(1, N + 1):
        # 현재 스테이지를 클리어하지 못한 유저 수
        fail = stage_counter[stage]
        
        # 분모 0 예외처리
        if total_players == 0:
            failure_rate = 0
        else:
            failure_rate = fail / total_players

        result.append((stage, failure_rate))
        total_players -= fail  # 다음 스테이지로 넘어갈 사람들

    # 실패율 기준으로 내림차순, 같으면 스테이지 번호 오름차순
    result.sort(key=lambda x: (-x[1], x[0]))
    return [stage for stage, _ in result]