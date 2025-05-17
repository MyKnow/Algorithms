from sys import stdin, stdout
from collections import deque

readline = stdin.readline

def dfs(edges, start):
    visited = [False] * len(edges)

    stack = [start]
    
    result = []
    while stack:
        current = stack.pop()

        if not visited[current]:
            visited[current] = True
            result.append(str(current))
            
            for node in sorted(edges[current], reverse=True):
                if not visited[node]:
                    stack.append(node)

    print(" ".join(result))

def bfs(edges, start):
    visited = [False] * len(edges)
    visited[start] = True
    
    queue = deque([start])

    result = [str(start)]
    while queue:
        current = queue.popleft()

        for node in sorted(edges[current]):
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                result.append(str(node))

    print(" ".join(result))

    return

N, M, V = map(int, readline().split())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    e1, e2 = map(int, readline().split())
    edges[e1].append(e2)
    edges[e2].append(e1)


dfs(edges, V)
bfs(edges, V)