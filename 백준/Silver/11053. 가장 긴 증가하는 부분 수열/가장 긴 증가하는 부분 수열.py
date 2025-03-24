N = int(input())
Ai = list(map(int, input().split()))

# DP 배열 (최대 길이를 저장)
dp = [1] * N  

gMax = 1  # LIS의 최대 길이

for i in range(1, N):
    for j in range(i):  # i번째 원소보다 앞에 있는 원소 탐색
        if Ai[j] < Ai[i]:  # 증가하는 관계를 만족해야 함
            dp[i] = max(dp[i], dp[j] + 1)
    
    gMax = max(gMax, dp[i])  # 최댓값 업데이트

print(gMax)