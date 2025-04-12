import sys

input = sys.stdin.readline
print = sys.stdout.write

# N, M: int
# description: An integer representing length of matrix "A"
# range: 1 ≤ N, M ≤ 100
N, M = map(int, input().split())

# A: list[list[int]]
# description: 2-Dimensional list that represents matrix "A"
# range: -100 ≤ A ≤ 100
A = list()

# Update A
for _ in range(N):
    A.append( list(map(int, input().split())) )

# M, K: int
# description: An integer representing length of matrix "B"
# range: 1 ≤ M, K ≤ 100
M, K = map(int, input().split())

# B: list[list[int]]
# description: 2-Dimensional list that represents matrix "B"
# range: -100 ≤ B ≤ 100
B = list()

# Update B
for _ in range(M):
    B.append( list(map(int, input().split())) )

for row in A:
    # tmp: list[int]
    # description: A list of integers to store result of matrix multiplication in each row
    # length: K
    # initial: 0
    tmp = [0 for _ in range(K)]

    # Double repeat statement for matrix "B"
    for y in range(K):
        for x in range(M):
            # Add row[y] times each column of B to tmp[y]
            tmp[y] += row[x] * B[x][y]

    # Print tmp
    print(f"{' '.join(map(str, tmp))}\n")