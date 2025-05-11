import sys

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

def dfs(v):
    # visited[i]: order when node i was visited (0 if not visited)
    visited = [0 for _ in range(N + 1)]
    stack = [v]
    order = 1

    while stack:
        node = stack.pop()
        if visited[node] == 0:
            visited[node] = order
            order += 1

           # Push adjacent nodes in ascending order
            # so that higher-numbered nodes are visited first (due to stack LIFO)
            for x in sorted(edges[node]):
                if visited[x] == 0:
                    stack.append(x)
                
    return visited

# Run DFS and print visit order for each node (1-indexed)
print("\n".join(map(str, dfs(R)[1:])))