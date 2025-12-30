# 요약
# 1. 체스판의 크기는 I * I이며, index는 0부터 시작한다.
# 2. (sx, sy) 좌표에 나이트가 위치하게 되며, (ex, ey)까지 도달해야 한다.

# 고려사항
# Q1. 최소 크기가 4*4인데, 이 경우에는 나이트가 원하는 위치로 이동할 수 있을까?
# A1. 불가능하다. 즉, 원하는 위치로 이동이 불가능한 케이스가 주어진다.
#
# Q2. 어떻게 "최소"로 이동했는 지 확인할 수 있을까?
# A2. BFS는 최단거리를 확인할 수 있다!

# 구현
# 1. 입력 초기화
# 2. sx, sy 좌표에서 현재 이동 가능한 범위를 deque에 넣는다.
# 3. 만약 현재 방문한 곳이 (ex, ey) 좌표라면 즉시 depth를 return한다.
# 3-1. deque가 비워질 때까지 찾지 못한 경우 0을 return한다.

from collections import deque

def bfs(start, end, limit):
    sx, sy = start
    ex, ey = end
    dq = deque([(sx, sy)])
    visited = [[0 for _ in range(limit)] for _ in range(limit)]

    while dq:
        cx, cy = dq.popleft()

        # 현재 위치가 목표지점인 경우
        if cx == ex and cy == ey:
            # 현재 깊이 반환
            return visited[cx][cy]

        for dx, dy in DIRS:
            # x, y -> 이동하려는 경로
            x, y = dx+cx, dy+cy

            # 이동 가능할 경우
            if (0 <= x < limit) and (0 <= y < limit) and (visited[x][y] == 0):
                visited[x][y] = visited[cx][cy] + 1
                dq.append((x, y))

    return 0

# 나이트 이동 방향 튜플(x, y)을 저장한 리스트
DIRS = [
    (-2, -1),
    (-1, -2),
    (1, -2),
    (2, -1),
    (2, 1),
    (1, 2),
    (-1, 2),
    (-2, 1),
]


# 1.
T = int(input())

for _ in range(T):
    I = int(input())
    start = map(int, input().split())
    end = map(int, input().split())

    print(bfs(start, end, I))