# N: int
# description: An integer that represents the number of items
# range: 1 ≤ N ≤ 100
#
# K: int
# description: An integer that represents the amount that the "준서" can carry
# range: 1 ≤ K ≤ 100,000
N, K = map(int, input().split())

# items: list(int, int)
# description: A list of (int, int) tuple to store (weight, value) pairs
# length: N
items = []

# Append each pairs in items list
for _ in range(N):
    # W: int
    # description: An integer that represents weight of item
    # range: 1 ≤ W ≤ 100,000
    #
    # V: int
    # description: An integer that represents value of item
    # range: 1 ≤ V ≤ 1,000
    W, V = map(int, input().split())
    items.append( (W, V) )

# dp: list
# description: A list of integer to store maximum sum of values at each weight
# length: K
dp = [0 for _ in range(K)]

for W, V in items:
    # pRow: list
    # description: A list of integer that represents previous dp
    # length: K
    pRow = dp.copy()

    # Iterate from 1 through K
    # k: current weight
    for k in range(1, K+1):
        # kIndex: index of current weight
        kIndex = k - 1
        
        # When current weight is bigger and same to item's weight
        if (k >= W):
            # Update dp[kIndex] to maximum value between
            # pRow[kIndex]: previous value at current weight
            # and
            # V + pRow[max(kIndex-W, 0)]: Sum of values between value of current item and previous item.
            dp[kIndex] = max(pRow[kIndex], V + pRow[max(kIndex-W, 0)])
        else:
            # Update dp[kIndex] to previous value at current weight
            dp[kIndex] = pRow[kIndex]

print(dp[-1])