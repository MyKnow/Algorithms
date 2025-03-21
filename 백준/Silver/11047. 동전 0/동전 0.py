import sys

input = sys.stdin.readline

# [int] N: An Integer that represents length of Ai (range: 1 ≤ N ≤ 10)
# [int] K: An Integer that represents the amount of money to be made (range: 1 ≤ K ≤ 100,000,000)
N, K = map(int, input().split())

# [list(int)] Ai: List of Integers that store amount of each coin
Ai = list()

# Update Ai until coin is smaller than K
for idx in range(N):
    coin = int(input())
    if (coin > K):
        break
    Ai.append( coin )

# Reverse Ai
Ai.sort(reverse=True)

# [int] count: number of coins
count = 0

for coin in Ai:
    # Exit when K is 0
    if (K == 0):
        break
    # Update count
    count += (K // coin)
    # Update K
    K %= coin

print(count)