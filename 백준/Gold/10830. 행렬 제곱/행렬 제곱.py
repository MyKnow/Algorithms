import sys

input = sys.stdin.readline
# print = sys.stdout.write

div = 1_000

N, B = map(int, input().split())

A = list()
for _ in range(N):
    A.append( list(map(int, input().split())) )
    
memo = {1:A}

def matrixProduct(a, b):
    global N, div

    results = []
    for row in a:
        tmp = [0 for _ in range(N)]

        for y in range(N):
            for x in range(N):
                tmp[y] += (row[x] % div) * (b[x][y] % div)
                tmp[y] %= div

        results.append( tmp )

    return results

def solution(exp):
    if exp in memo:
        return memo[exp]
    else:
        result = solution(exp//2)
        memo[exp] = matrixProduct(result, result)
        
        if exp % 2 == 0:
            return memo[exp]
        else:
            return matrixProduct(memo[exp], memo[1])

for row in solution(B):
    for col in row:
        print(col % div, end=" ")
    print()