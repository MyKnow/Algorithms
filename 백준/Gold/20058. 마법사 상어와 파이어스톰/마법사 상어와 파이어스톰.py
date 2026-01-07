# 문제 요약
# 길이가 2^N인 정사각형 얼음판에서 파이어스톰을 연습한다.
# A[r][c]는 격자의 r행 c열에 있는 얼음의 양을 의미하며, 0은 얼음이 없는 것이다.
# 파이어스톰을 시전할 때는 단계(L)을 결정한다.
# 1. 2^L 길이의 정사각형 격자로 얼음판을 나누고, 그 후 모든 부분 격자를 시계 방향으로 90도 회전시킨다.
# 2. 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다. (상하좌우)
# 마법사 상어가 파이어스톰을 Q번 시전한 뒤의 
# 1. 남아있는 얼음의 합
# 2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
# 를 구해야 한다.
# 얼음이 있는 칸이 얼음이 있는 칸과 인접(동서남북)해 있으면, 두 칸을 연결되어 있다고 한다.

# 이해가 안되는 포인트
# Q1. 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다. (상하좌우)
# A1. => 동서남북에 얼음이 3개 이상 없으면, 그 칸은 -1 처리

# 회전 시키는 방법
# ! 격자는 얼음판보다 크지 않다.
# ! 얼음판과 동일한 크기나 0도 주어진다.
#
# 예시 ( L=1, 시작=(3, 1) )
# (3, 1), (4, 1),
# (3, 2), (4, 2),
# ->
# (3, 2), (3, 1),
# (4, 2), (4, 1),
# 
# 예시 ( L=2, 시작=(1, 1) )
# (1, 1), (2, 1), (3, 1), (4, 1),
# (1, 2), (2, 2), (3, 2), (4, 2),
# (1, 3), (2, 3), (3, 3), (4, 3),
# (1, 4), (2, 4), (3, 4), (4, 4),
#
# -> 이제 보니깐 각 열을 역순으로 뒤집은 다음, 행으로 넣으면 된다!!

# 동서남북 (r, c)
DIRS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

# 구현
# 1. N, Q, A, L을 입력 받는다.
# 2. Q번 반복한다.
    # 2-1. (0, 0)부터 2**L칸 떨어진 곳을 격자의 좌상단으로 가정하고, 모든 격자를 시계방향으로 회전시킨다.
    # 2-2. A를 순회하며 동서남북 칸이 0이 아닌 칸의 개수를 세고, 3개 미만이면 현재 칸을 1 감소시킨다.
# 3. A를 순회하며 A의 총합을 구한다.
# 4. A를 순회하며 bfs값을 구한다.(이미 방문처리 되어 있으면 생략한다.)
    # 이 때 bfs 중 가장 큰 값을 업데이트한다.

from collections import deque

# 1
N, Q = map(int, input().split())
LEN_A = 2**N
A = [list(map(int, input().split())) for _ in range(LEN_A)]
L = list(map(int, input().split()))

# 2
for l in L:
    # 2-1
    interval = 2**l
    if l != 0:
        for r in range(0, LEN_A, interval):
            for c in range(0, LEN_A, interval):
                sub = [row[c:c+interval] for row in A[r:r+interval]]
                rot = list(zip(*sub[::-1]))
                for i in range(interval):
                    A[r+i][c:c+interval] = rot[i]

    # 2-2
    melt_pos = []
    for r in range(LEN_A):
        for c in range(LEN_A):
            count = 0

            if A[r][c] == 0:
                continue
            
            for dr, dc in DIRS:
                sr, sc = r+dr, c+dc
                if (0 <= sr < LEN_A) and (0 <= sc < LEN_A) and (A[sr][sc] != 0):
                    if count >= 3:
                        break
                    count += 1
            if count < 3:
                melt_pos.append( (r, c) )
                
    for r, c in melt_pos:
        A[r][c] = max(0, A[r][c]-1)

# 3
total = 0
for row in A:
    total += sum(row)

# 4
visited = [[False for _ in range(LEN_A)] for _ in range(LEN_A)]
def bfs(r, c):
    dq = deque([(r, c)])
    visited[r][c] = True
    count = 1

    while dq:
        cr, cc = dq.popleft()

        for dr, dc in DIRS:
            sr, sc = cr+dr, cc+dc

            if (0 <= sr < LEN_A) and (0 <= sc < LEN_A) and (A[sr][sc] != 0) and not visited[sr][sc]:
                visited[sr][sc] = True
                count += 1
                dq.append((sr, sc))

    return count

max_bfs = 0
for r in range(LEN_A):
    for c in range(LEN_A):
        if A[r][c] > 0 and not visited[r][c]:
            max_bfs = max(max_bfs, bfs(r, c))

print(total)
print(max_bfs)
