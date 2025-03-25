# N: int
# description: An integer that represents length of Ai
# range: 1 ≤ N ≤ 1,000
N = int(input())

# Ai: list(int)
# description: A list of integers that stores sequences for finding bitonic sequences
# length: N
# range: 1 ≤ Ai ≤ 1,000
Ai = list(map(int, input().split()))

# dp: list(int)
# description: A list of integers to store lengths of LIS for each index
# length: N
dp = [1] * N

# reverseDP: list(int)
# description: A list of integers to store lengths of LDS for each index
# length: N
reverseDP = [1] * N

# Update dp
for i in range(N):
    for j in range(i):
        if Ai[i] > Ai[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# Update reverseDP
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if Ai[i] > Ai[j]:
            reverseDP[i] = max(reverseDP[i], reverseDP[j] + 1)

# Print by subtracting 1 from the maximum value from the sum of dp and reverseDP
print(max(map(sum, zip(dp, reverseDP)))-1)