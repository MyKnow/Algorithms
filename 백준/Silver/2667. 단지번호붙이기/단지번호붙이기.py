from sys import stdin
from collections import deque

readline = stdin.readline

N = int(readline())

edges = [[] for _ in range(N)]
for y in range(N):
    line = readline().rstrip()
    for x in line:
        edges[y].append(int(x))


def bfs(edges, x, y):
    dq = deque()
    dq.append( (x, y) )
    length = 1
    
    while dq:
        currentX, currentY = dq.popleft()
        edges[currentY][currentX] = 0

        top = (currentY != 0) and edges[currentY-1][currentX] == 1
        bot = (currentY != len(edges)-1) and edges[currentY+1][currentX] == 1
        left = (currentX != 0) and edges[currentY][currentX-1] == 1
        right = (currentX != len(edges)-1) and edges[currentY][currentX+1] == 1

        if top:
            dq.append( (currentX, currentY-1) )
            edges[currentY-1][currentX] = 0
            length += 1
        if bot:
            dq.append( (currentX, currentY+1) )
            edges[currentY+1][currentX] = 0
            length += 1
        if left:
            dq.append( (currentX-1, currentY) )
            edges[currentY][currentX-1] = 0
            length += 1
        if right:
            dq.append( (currentX+1, currentY) )
            edges[currentY][currentX+1] = 0
            length += 1

    return length


result = []
for y in range(N):
    for x in range(N):
        if edges[y][x] == 1:
            result.append( bfs(edges, x, y) )

print(len(result))
print("\n".join(map(str, sorted(result))))