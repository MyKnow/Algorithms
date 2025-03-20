# [int] n: An Integer that represents height of triangle
n = int(input())

# [list(list(int))] dp: 2-Dimensional list of integers that stores values in triangle
dp = list()

# Append values in triangle to dp
for _ in range(n):
    dp.append ( list(map(int, input().split())) )

for idx in range(1, n):
    for vIdx, val in enumerate(dp[idx]):
        left = 0
        right = 0
        # Update left when exist value in the top left
        if (vIdx != 0):
            left = dp[idx-1][vIdx-1]
        # Update right when exist value in the top right
        if (vIdx != len(dp[idx])-1):
            right = dp[idx-1][vIdx]

        # Update the current value by adding the larger value of top left or top right and the value in current position
        dp[idx][vIdx] = max(left, right) + val

# Print maximum value in dp
print(max(dp[n-1]))