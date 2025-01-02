# N: int - 세준이가 시험을 본 과목의 개수 (1? <= N <= 1000)
N = int(input())

# scoreList: list - 세준이의 시험 점수들 (길이: N, 0 < score <= 100)
scoreList = list(map(int, input().split()))

# M: int - 세준이의 시험 점수 중 최고점인 것 (0 < M <= 100)
M = max(scoreList)

# replacedScoreList: list - 각 과목의 점수를 점수/M*100으로 고친 list
replacedScoreList = [(x/M*100) for x in scoreList]

# 평균을 산출한다.
print(sum(replacedScoreList)/len(replacedScoreList))
