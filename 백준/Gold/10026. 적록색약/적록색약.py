from collections import deque

# 상, 하, 좌, 우
dir_y = [-1, 1, 0, 0]
dir_x = [0, 0, -1, 1]

def solution(N, M):
    visited = [[False for _ in range(N)] for _ in range(N)]
    result = 0
    
    for y in range(N):
        for x in range(N):
            crt_color = M[y][x]
            if not visited[y][x]:
                dq = deque([(y, x)])
                visited[y][x] = True
                result += 1

                while(dq):
                    cy, cx = dq.popleft()
                    
                    for dy, dx in zip(dir_y, dir_x):
                        sy, sx = dy+cy, dx+cx

                        if (0 <= sy < N) and (0 <= sx < N) and not visited[sy][sx] and crt_color == M[sy][sx]:
                            dq.append( (sy, sx) )
                            visited[sy][sx] = True      

    print(result)


if __name__ == "__main__":
    N = int(input())
    normal = []
    trans = []
    for _ in range(N):
        row = input()
        normal.append(list(row))
        trans.append( row.replace("G", "R") )

    solution(N, normal)
    solution(N, trans)