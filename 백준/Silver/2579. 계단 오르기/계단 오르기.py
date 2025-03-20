# [int] n: An Integer that represents number of stairs
n = int(input())

# [list(int)] stairs: List of integers that stores values of each stairs
stairs = list()
stairs.append(0)

# Append values of each stairs
for _ in range(n):
    stairs.append ( int(input()) )

# [list(int)] dp: List of integers that stores calculated values
dp = [0] * (n+1)
dp[0] = stairs[0]
dp[1] = dp[0] + stairs[1]

for idx in range(2, n+1):
    # Update dp[idx] with sum of the current step values and larger value between "oneStep" and "twoStep"
    twoStep = dp[idx-3] + stairs[idx-1]
    ownStep = dp[idx-2]
    dp[idx] = max(ownStep, twoStep) + stairs[idx]

# Print nth dp
print(dp[n])