import bisect
import sys

def getLIS(A):
    dp = []
    lisLength = [0] * len(A)

    for i in range(len(A)):
        idx = bisect.bisect_left(dp, A[i][1])

        if idx == len(dp):
            dp.append(A[i][1])
        else:
            dp[idx] = A[i][1]
        lisLength[i] = idx + 1
        
    return lisLength

input = sys.stdin.readline

N = int(input())

lines = list()

for _ in range(N):
    A, B = map(int, input().split())

    lines.append( (A, B) )

lines.sort(key=lambda x: x[0])

lis = getLIS(lines)

print(N-max(lis))