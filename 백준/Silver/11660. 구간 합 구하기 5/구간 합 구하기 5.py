import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

pSum = [[0 for _ in range(N+1)] for _ in range(N+1)]

for y in range(1, N+1):
    lines = list(map(int, input().split()))

    for x in range(1, N+1):
        pSum[y][x] = lines[x-1] + pSum[y-1][x] + pSum[y][x-1] - pSum[y-1][x-1]
        
results = []
for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())

    results.append ( pSum[y2][x2] - pSum[y2][x1- 1] - pSum[y1-1][x2] + pSum[y1-1][x1-1] )

print("\n".join(map(str, results))+"\n")