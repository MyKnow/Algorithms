import sys

# Increase recursion limit to avoid RecursionError
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# N: number of nodes
# M: number of edges
# R: start node
N, M, R = map(int, input().split())

# edges[i]: list of adjacent nodes of node i
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

# Sort adjacency list in ascending order to ensure answers
for i in range(1, N + 1):
    edges[i].sort()

# visited[i]: order when node i was visited
visited = [0 for _ in range(N + 1)]
order = 1

def dfs(v):
    global order
    visited[v] = order

    for x in edges[v]:
        if visited[x] == 0:
            order += 1
            dfs(x)

# Start DFS
dfs(R)

# Output visit order for all nodes
for i in range(1, N + 1):
    print(visited[i])