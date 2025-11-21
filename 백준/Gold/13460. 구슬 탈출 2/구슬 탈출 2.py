# 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임

# 보드
# 세로: N (3 이상)
# 가로: M (10 이상)
# 1*1 칸
# 가장 바깥 행·열은 모두 막혀 있다.
# 구멍이 하나 있다.
# 파란 구슬이 구멍에 들어가면 안된다.
# 중력을 이용해서 이리 저리 굴려야 한다. (상, 하, 좌, 우)
# 공은 모두 동시에 움직인다.
# 빈칸: .
# 벽: #
# 구멍: O
# 빨간구슬: R
# 파란구슬: B

# 예외처리
# - 10번 이하로 빨간 구슬을 빼낼 수 없는 경우
from collections import deque
import sys
input = sys.stdin.readline

# dx, dy: 상하좌우
DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def solve():
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]

    # R, B 초기 위치
    rx = ry = bx = by = -1
    for y in range(N):
        for x in range(M):
            if board[y][x] == 'R':
                rx, ry = x, y
            elif board[y][x] == 'B':
                bx, by = x, y

    q = deque()
    q.append((rx, ry, bx, by, 0))

    visited = set()
    visited.add((rx, ry, bx, by))

    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth >= 10:
            continue

        for dx, dy in DIR:
            # R 이동
            nrx, nry = rx, ry
            r_move = 0
            r_out = False
            while True:
                nx = nrx + dx
                ny = nry + dy
                if board[ny][nx] == '#':
                    break
                nrx, nry = nx, ny
                r_move += 1
                if board[nry][nrx] == 'O':
                    r_out = True
                    break

            # B 이동
            nbx, nby = bx, by
            b_move = 0
            b_out = False
            while True:
                nx = nbx + dx
                ny = nby + dy
                if board[ny][nx] == '#':
                    break
                nbx, nby = nx, ny
                b_move += 1
                if board[nby][nbx] == 'O':
                    b_out = True
                    break

            # 파란 구슬 빠지면 실패
            if b_out:
                continue

            # 빨간 구슬만 빠지면 성공
            if r_out:
                print(depth + 1)
                return

            # 둘이 같은 위치면, 더 많이 이동한 구슬을 한 칸 뒤로
            if nrx == nbx and nry == nby:
                if r_move > b_move:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            # 방문 체크
            state = (nrx, nry, nbx, nby)
            if state not in visited:
                visited.add(state)
                q.append((nrx, nry, nbx, nby, depth + 1))

    print(-1)


if __name__ == "__main__":
    solve()