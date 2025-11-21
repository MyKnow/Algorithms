# 뱀 게임
# 벽 또는 자기자신의 몸과 부딪히면 게임이 끝남
# NxN 정사각 보드(벽 존재)
# 몇몇 칸에 사과 있음
# 뱀 초기에 상단 좌측에 위치, 길이 1, 우측 향함

# 이동 규칙
# 1. 몸 길이를 늘려서 머리를 다음 칸에 위치 시킨다.
# 2. 다음 칸에
#   - 벽이나 자기자신의 몸과 부딪히면 게임이 끝남.
#   - 사과가 있었다면
#       - 그 칸에 있었던 사과가 없어지고 꼬리는 움직이지 않음
#       - 꼬리가 위치한 칸을 비운다.

# 입력
# 1. 보드 크기: 2 ≤ N ≤ 100
# 2. 사과 개수: 0 ≤ K ≤ 100
# 3. K개의 줄에 사과의 위치: "행 열"
# 4. 방향 변환 횟수: 1 ≤ L ≤ 100
# 5. L개의 줄에 방향 변환 정보: "X C"
#   - X: 게임 시작 시간으로부터 지난 시간 (10,000 이하의 양의 정수, 순서대로 처리하면 된다.)
#   - C: 회전 방향(L: 왼쪽, D: 오른쪽)

# 출력:
# 게임이 끝나는 시각

# 흐름
# 1. 게임의 최대 길이는 10,000+a 일 것 같은데, 시간 초과가 일어날 것 같지는 않으므로 실시간 처리한다.
# 2. 게임을 1틱씩 진행하며 매 순간마다 이동 규칙을 체크한다.

from collections import deque

def solve():
    N = int(input())
    K = int(input())
    apples = set([tuple(map(int, input().split())) for _ in range(K)])
    L = int(input())
    dirs = dict()
    for _ in range(L):
        X, C = input().split()
        dirs[int(X)] = C

    # 1. 현재 진행 방향 index
    # 2. 각 몸 위치(y, x)
    snake = deque([(1, 1)])
    turns = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
    for t in range(1, 10_000):
        # 이동 방향에 새로운 몸 위치 계산
        head_y, head_x = snake[0]
        next_head = (head_y+turns[0][0], head_x+turns[0][1])

        # 해당 위치에 몸이 있거나 범위 밖이라면 종료
        if (next_head in snake) or not (0 < next_head[0] <= N and 0 < next_head[1] <= N):
            return t

        # 현재 자리를 머리로 넣는다.
        snake.appendleft(next_head)
        if next_head in apples:
            apples.remove(next_head)
        else:
            # 아무것도 없다면 원래 자리를 지운다.
            snake.pop()

        # 방향 전환 검사
        if t in dirs:
            val = (1 if dirs[t] == "L" else -1)
            turns.rotate(val)

if __name__ == "__main__":
    print(solve())
