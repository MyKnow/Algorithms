import sys

input = sys.stdin.readline
# print = sys.stdout.write

# div: int
# description: An integer that performs each element and the 
# rest of the operation in the matrix multiplication operation
# initial: 1,000
div = 1_000

# N: int
# description: An integer that represents size of matrix
# range: 2 ≤ N ≤  5
#
# B: int
# description: An integer that represents number 
# of times the matrix will be squared
# range: 1 ≤ B ≤ 100,000,000,000
N, B = map(int, input().split())

# A: list[list[int]]
# description: 2-Dimensional list of integers that stores matrix 
# used for matrix squared operations
# length: N * N
A = list()
for _ in range(N):
    A.append( list(map(int, input().split())) )

# memo: dict(int, list[list[int]])
# description: A dictionary to store each 
# results of matrix power by exponent
# key -> exponent: int
# value -> matrix: list[list[int]]
# initial: 1: A
memo = {1:A}

# matrixProduct: def(a: list[list[int]], b: list[list[int]]) -> results: list[list[int]]
# description: A function that returns of multiplying the matrix
# a and b using the remaining operations
def matrixProduct(a, b):
    # results: List of integers for saving and returning results
    results = []

    for row in a:
        tmp = [0 for _ in range(N)]

        for y in range(N):
            for x in range(N):
                # Multiply a and b with Using remainder operations 
                tmp[y] += (row[x] % div) * (b[x][y] % div)
                tmp[y] %= div
        
        results.append( tmp )

    return results

# solution: def(exp: int) -> list[list[int]]
# description: A function that returns a matrix squared by given exponent
def solution(exp):
    # Using memoization
    if exp in memo:
        return memo[exp]
    else:
        # result: A result of matrix squared by exponent//2 
        result = solution(exp//2)
        
        # Store the result of result matrix squared by into memo[exp]
        memo[exp] = matrixProduct(result, result)

        # Exponential law
        if exp % 2 == 0:
            return memo[exp]
        else:
            return matrixProduct(memo[exp], memo[1])

# Print answer
for row in solution(B):
    for col in row:
        print(col % div, end=" ")
    print()