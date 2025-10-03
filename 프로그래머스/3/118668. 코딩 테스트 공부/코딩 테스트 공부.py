# [alp_req, cop_req, alp_rwd, cop_rwd, cost]
# [필요 알고력, 필요 코딩력, 증가 알고력, 증가 코딩력, 풀이시간]
#
# 모든 문제를 풀 수 있는 알고력과 코딩력을 얻는 최단시간 구하기
# : 모든 문제를 풀어야 하는 게 아니라, 목표 알고력과 코딩력을 충족하면 됨.
#
def solution(alp, cop, problems):
    # 우선 목표 알고력, 목표 코딩력 산출
    alp_tar, cop_tar = 0, 0
    for problem in problems:
        alp_tar = max(problem[0], alp_tar)
        cop_tar = max(problem[1], cop_tar)
        
    # 시작값이 목표치를 넘을 수 있으므로 상한선으로 클램핑
    alp = min(alp, alp_tar)
    cop = min(cop, cop_tar)
        
    # dp[alp][cop]: 해당 알고력, 코딩력에 도달하기 위해 필요한 시간
    dp = [[10**9 for _ in range(cop_tar+1)] for _ in range(alp_tar+1)]
    dp[alp][cop] = 0
    
    # 최초 alp, cop부터 목표 alp, cop까지 쭉 계산한다.
    for a in range(alp, alp_tar+1):
        for c in range(cop, cop_tar+1):
            # 1. 풀 수 있는 문제가 없어서 시간을 소비하여 공부할 때
            # 범위 체크 및 기존 값보다 단순 공부가 효율이 좋은 지 확인해야 한다.
            if (a + 1 <= alp_tar) and (dp[a+1][c] > dp[a][c] + 1):
                dp[a+1][c] = dp[a][c]+1
            if (c + 1 <= cop_tar) and (dp[a][c+1] > dp[a][c] + 1):
                dp[a][c+1] = dp[a][c]+1
                
            # 2. 문제 풀기
            # 전체 문제를 순회하며 문제를 풀어 풀이 능력을 올린 결과를 저장한다.
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                
                # 풀 수 있는 문제인 경우 문제를 푼다.
                if a >= alp_req and c >= cop_req:
                    # 범위를 벗어나면 안되므로, min을 통해 클램핑
                    sa = min(a+alp_rwd, alp_tar)
                    sc = min(c+cop_rwd, cop_tar)
                    
                    # 이전 경우보다 효율적인 경우에만 업데이트
                    if dp[sa][sc] > dp[a][c] + cost:
                        dp[sa][sc] = dp[a][c] + cost
                        
    return dp[alp_tar][cop_tar]