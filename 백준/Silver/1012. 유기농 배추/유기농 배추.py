from sys import stdin
from collections import deque

readline = stdin.readline

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(field, points):
    worm = 0

    while points:
        worm += 1
        firstX, firstY = points.pop()
        dq = deque( [ (firstX, firstY) ] )

        while dq:
            cx, cy = dq.popleft()
            
            for x, y in directions:
                dx, dy = cx+x, cy+y
    
                if 0 <= dy < len(field) and 0 <= dx < len(field[0]) and field[dy][dx] == 1:
                    if (dx, dy) in points:
                        points.remove( (dx, dy) )
                        
                    field[dy][dx] = 0
                    dq.append( (dx, dy) )

    return worm
    
def solution():
    T = int(readline())
    
    for _ in range(T):
        M, N, K = map(int, readline().split())
    
        field = [[0 for _ in range(M)] for _ in range(N)]
        points = set()
        for _ in range(K):
            X, Y = map(int, readline().split())
            points.add( (X, Y) )
            field[Y][X] = 1
    
        print(bfs(field, points))

solution()