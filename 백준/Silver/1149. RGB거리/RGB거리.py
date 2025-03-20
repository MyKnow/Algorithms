# [int] n: An Integer that represents number of houses
n = int(input())

# [list(int)] dp: 2-Dimensional list of integers that stores RGB painting cost value of each houses
dp = list()

for _ in range(n):
    # Append RGB painting cost values to dp
    dp.append(list(map(int, input().split())))

# Update DP
for idx in range(1, n):
    dp[idx][0] = min(dp[idx-1][1], dp[idx-1][2]) + dp[idx][0]
    dp[idx][1] = min(dp[idx-1][0], dp[idx-1][2]) + dp[idx][1]
    dp[idx][2] = min(dp[idx-1][0], dp[idx-1][1]) + dp[idx][2]

# Print minimum at dp[n-1]
print(min(dp[n-1]))