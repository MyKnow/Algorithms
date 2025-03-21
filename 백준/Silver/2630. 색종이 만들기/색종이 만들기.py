import sys

input = sys.stdin.readline

N = int(input())

paper = list()

for _ in range(N):
    paper.append( list(map(int, input().split())) )

bCount = 0
wCount = 0

def solution(n: int, m: list(list())):
    global bCount, wCount

    sumOfPaper = 0
    for row in m:
        sumOfPaper += sum(row)

    if (sumOfPaper == n * n):
        bCount += 1
    elif (sumOfPaper == 0):
        wCount += 1
    else:
        for p in divide(n, m):
            solution(n//2, p)

def divide(n: int, m: list(list())):
    topLeft = [[0 for _ in range(n//2)] for _ in range(n//2)]
    topRight = [[0 for _ in range(n//2)] for _ in range(n//2)]
    botLeft = [[0 for _ in range(n//2)] for _ in range(n//2)]
    botRight = [[0 for _ in range(n//2)] for _ in range(n//2)]

    for y in range(n):
        for x in range(n):
            if x < (n // 2):
                if y < (n // 2):
                    topLeft[y][x] = m[y][x]
                else:
                    botLeft[y-(n // 2)][x] = m[y][x]
            else:
                if y < (n // 2):
                    topRight[y][x-(n // 2)] = m[y][x]
                else:
                    botRight[y-(n // 2)][x-(n // 2)] = m[y][x]
    return topLeft, topRight, botLeft, botRight


solution(N, paper)

print(wCount)
print(bCount)