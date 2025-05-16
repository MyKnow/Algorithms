from collections import deque
from sys import stdin, stdout

readline = stdin.readline
        
C = int(readline())
P = int(readline())

edges = [[] for _ in range(C+1)]

for _ in range(P):
    u, v = map(int, readline().split())

    edges[u].append(v)
    edges[v].append(u)


def bfs(edges, r):
    visited = [False for _ in range(C+1)]
    total = -1
    
    dq = deque()
    dq.append(r)

    while dq:
        node = dq.popleft()

        for n in sorted(edges[node], reverse=True):
            if (not visited[n]):
                visited[n] = True
                total += 1
                dq.append(n)

    return max(total, 0)

print(bfs(edges, 1))