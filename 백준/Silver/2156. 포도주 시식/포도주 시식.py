import sys

input = sys.stdin.readline

# [int] n: number of glass (range: 1 ≤ n ≤ 10,000)
n = int(input())

# [list(int)] glass: List of integers that store amount of wine at each glass (range: ≤ 1,000, length: n)
glass = [int(input()) for _ in range(n)]

# [list(int)] dp: List of integers to store the total amount of wine drinked by each index
dp = [0] * (n)
dp[0] = glass[0]

# Protection of IndexError
if len(dp) != 1:
    dp[1] = glass[0] + (glass[1] if len(glass) > 1 else 0)

for idx in range(2, n):
    # Cases:
    # 1. Not drinking current wine
    # 2. Drinking idx-2 wine and current wine
    # 3. Drinking before and current wine
    # Update dp[idx] to largest of the three cases.
    dp[idx] = max( dp[idx-1], dp[idx-2]+glass[idx], (dp[idx-3] if n != 2 else 0) +glass[idx-1]+glass[idx] )

print(max(dp))