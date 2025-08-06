from sys import stdin
from collections import deque

readline = stdin.readline

# 4방향 정의
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(M, N, maze):
    # 재방문 여부 기록
    visited = [[False for _ in range(M)] for _ in range(N)]

    # 시작점 업데이트
    dq = deque([(0, 0)])
    visited[0][0] = True

    while dq:
        cx, cy = dq.popleft()
        cDepth = maze[cy][cx]
        
        for dx, dy in directions:
            sx, sy = cx+dx, cy+dy

            # 유효 범위 체크
            if 0 <= sx < M and 0 <= sy < N and maze[sy][sx] != 0 and not visited[sy][sx]:
                visited[sy][sx] = True
                maze[sy][sx] = cDepth + 1
                
                # 종료 조건
                if sx == (M-1) and sy == (N-1):
                    return maze[N-1][M-1]
                    
                dq.append((sx, sy))


def solution():
    # 세로, 가로
    N, M = map(int, readline().split())
    
    # 미로 초기화
    maze = [list(map(int, readline().rstrip())) for _ in range(N)]

    print(bfs(M, N, maze))

solution()