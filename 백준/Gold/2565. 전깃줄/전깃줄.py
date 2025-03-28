import bisect
import sys

input = sys.stdin.readline

# [def(list(tuple)) -> list] getLIS
# : A function that finds LIS list from typle list to return list: called as lines
#
# - Parameters
# 1. A: list(tuple)
# description: List of tuples that stores electir wires connected to A and B poles
# 
# - Returns
# 1. lisLength: list
# description: List of integers that stores the length of LIS obtained from each index
def getLIS(A: list( (int, int) )):
    # B: list
    # description: List of integers to store positions of wires from pole B
    dp = []

    for i in range(len(A)):
        # idx: int
        # Index indicating where the wire can be inserted now
        idx = bisect.bisect_left(dp, A[i][1])

        # When idx is the last index
        if idx == len(dp):
            # Just append it
            dp.append(A[i][1])
        else:
            # Update already existing elements
            dp[idx] = A[i][1]

    return len(dp)

# N: int
# description: An integer that represents number of electric wires
N = int(input())

# wires: list( (int, int) )
# description: A list of tuples to store electric wires connected to A and B poles
wires = list()

# Update wires
for _ in range(N):
    A, B = map(int, input().split())

    wires.append( (A, B) )

# Sort in ascending order by pole A
wires.sort(key=lambda x: x[0])

# Get length of LIS of wires
lengthOfLIS = getLIS(wires)

# Print result
print(N-lengthOfLIS)