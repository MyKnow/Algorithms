# [int] X: An integer that represents number to finding number of calculations
# : (range: 1 ≤ X ≤ 10^6)
X = int(input())

# [list(int)] dp: List of integers to store numbers of calculations in each index
dp = [0] * (X+1)
# 1 dosn't require calculation.
dp[1] = 0

# Repeat from 2 to (X+1)
for idx in range(2, X+1):
    # Each cases
    # 1. "idx" isn't divided into 2 or 3.
    dp[idx] = 1 + dp[idx-1]
    
    # 2. "idx" divided into 3
    if idx % 3 == 0:
        dp[idx] = min(dp[idx], dp[idx//3] + 1)
    # 3. "idx" divided into 2
    if idx % 2 == 0:
        dp[idx] = min(dp[idx], dp[idx//2] + 1)

print(dp[X])