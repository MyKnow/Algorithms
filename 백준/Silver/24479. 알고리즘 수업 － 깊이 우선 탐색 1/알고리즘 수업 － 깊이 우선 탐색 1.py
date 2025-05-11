import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

edges = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
    
for i in range(1, N+1):
    edges[i].sort()

visited = [0 for _ in range(N+1)]
order = 1

def dfs(v):
    global order
    visited[v] = order

    for x in edges[v]:
        if visited[x] == 0:
            order += 1
            dfs(x)

dfs(R)

for i in range(1, N + 1):
    print(visited[i])