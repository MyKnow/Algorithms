from collections import deque
from sys import stdin, stdout

readline = stdin.readline
        
N, M, R = map(int, readline().split())

edges = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, readline().split())

    edges[u].append(v)
    edges[v].append(u)


def bfs(edges, r):
    order = 1
    
    visited = [0 for _ in range(N+1)]
    visited[r] = order
    
    dq = deque()
    dq.append(r)

    while dq:
        node = dq.popleft()

        for n in sorted(edges[node], reverse=True):
            if (visited[n] == 0):
                order += 1
                visited[n] = order
                dq.append(n)

    return visited[1:]

print("\n".join(map(str, bfs(edges, R))))