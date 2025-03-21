import sys

input = sys.stdin.readline

# [int] N: An Integer that represents length of mapOfN
# [int] M: An Integer that represents count of test cases
N, M = map(int, input().split())

# [map(int)] mapOfN: Map of Integers that stores nature numbers to find prefix sum
mapOfN = map(int, input().split())

# [list(int)] prefixSum: List of Integers that stores prefix sum of mapOfN
prefixSum = [0]

# Update prefixSum
for idx, n in enumerate(mapOfN):
    prefixSum.append( n + prefixSum[idx] )

for _ in range(M):
    i, j = map(int, input().split())

    # Calculate sum of sections i to j
    print(prefixSum[j] - prefixSum[i-1])