import sys
input = sys.stdin.readline

def main():
    N, M, x, y, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    orders = list(map(int, input().split()))

    # dice indices: 1=상단, 2=북쪽, 3=동쪽, 4=서쪽, 5=남쪽, 6=바닥 
    dice = [0] * 7

    # direction deltas: index by command 1..4 (1=동, 2=서, 3=북, 4=남)
    dr = [0, 0, 0, -1, 1]
    dc = [0, 1, -1, 0, 0]

    r, c = x, y

    out_lines = []
    for cmd in orders:
        nr = r + dr[cmd]
        nc = c + dc[cmd]

        # 바깥이면 명령 무시 (출력도 하지 않음)
        if not (0 <= nr < N and 0 <= nc < M):
            continue

        # 주사위 면 회전 (정석적 인덱스 교체)
        if cmd == 1:  # 동 
            tmp = dice[1]
            dice[1] = dice[4]
            dice[4] = dice[6]
            dice[6] = dice[3]
            dice[3] = tmp
        elif cmd == 2:  # 서 
            tmp = dice[1]
            dice[1] = dice[3]
            dice[3] = dice[6]
            dice[6] = dice[4]
            dice[4] = tmp
        elif cmd == 3:  # 북 
            tmp = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[6]
            dice[6] = dice[2]
            dice[2] = tmp
        elif cmd == 4:  # 남 
            tmp = dice[1]
            dice[1] = dice[2]
            dice[2] = dice[6]
            dice[6] = dice[5]
            dice[5] = tmp

        # 위치 갱신
        r, c = nr, nc

        # MAP과 주사위 바닥면 상호작용
        if MAP[r][c] == 0:
            MAP[r][c] = dice[6]
        else:
            dice[6] = MAP[r][c]
            MAP[r][c] = 0

        out_lines.append(str(dice[1]))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()