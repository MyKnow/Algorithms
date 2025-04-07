import sys
	
input = sys.stdin.readline
print = sys.stdout.write

# N, M: int
# description: Integers representing lengths of table: vertical, horizontal
# range: 1 ≤ N, M ≤ 2,000
#
# K: int
# description: An integer representing length of the new chessboard that jimin will make
# range: 1 ≤ K ≤ min(N, M)
N, M, K = map(int, input().split())

# pSumOfB, pSumOfW: list(list(int))
# description: 2-Dimensional lists of integers to store prefix sums that representing 
# total number of repainting times in an incorrectly colored compartment.
# length: (M+1) * (N+1)
pSumOfB = [[0 for _ in range(M+1)] for _ in range(N+1)]
pSumOfW = [[0 for _ in range(M+1)] for _ in range(N+1)]

for y in range(1, N+1):
    # line: If the color of the board compartment is Black
    # it is True, otherwise False
    line = list(map(lambda x: x == "B", [c for c in input().rstrip()]))

    # crtB: Correct color of "black first board" in each index y
    # crtW: Correct color of "white first board" in each index y
    crtB = (True if y % 2 == 1 else False)
    crtW = not crtB

    for x in range(1, M+1):
        # If the current color is incorrect, add the sum of 1 and
        # 2D prefixes and update the current pSum.
        pSumOfB[y][x] = (0 if line[x-1] == crtB else 1) + pSumOfB[y-1][x] + pSumOfB[y][x-1] - pSumOfB[y-1][x-1]
        pSumOfW[y][x] = (0 if line[x-1] == crtW else 1) + pSumOfW[y-1][x] + pSumOfW[y][x-1] - pSumOfW[y-1][x-1]

        # Change the color of each variable to the opposite color.
        crtB = not crtB
        crtW = not crtW

# minOfB, minOfW: float
# description: A floats to store minimum value of each pSum
minOfB = float('inf')
minOfW = float('inf')

for yK in range(K, N+1):
    for xK in range(K, M+1):
        # sumOfB, sumOfW: Prefix sum of each color on (xK, yK) points
        sumOfB = pSumOfB[yK][xK] - pSumOfB[yK-K][xK] - pSumOfB[yK][xK-K] + pSumOfB[yK-K][xK-K]
        sumOfW = pSumOfW[yK][xK] - pSumOfW[yK-K][xK] - pSumOfW[yK][xK-K] + pSumOfW[yK-K][xK-K]

        # Update minOfB and minOfW to smallest value
        minOfB = min(minOfB, sumOfB)
        minOfW = min(minOfW, sumOfW)

# Print minimum value between minOfW and minOfB
print(str(min(minOfW, minOfB))+"\n")