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
                result += 1

                while(dq):
                    cy, cx = dq.pop()
                    visited[cy][cx] = True
                    

                    for i in range(len(dir_y)):
                        dy, dx = dir_y[i]+cy, dir_x[i]+cx

                        if (0 <= dy < N) and (0 <= dx < N) and not visited[dy][dx] and crt_color == M[dy][dx]:
                            dq.append( (dy, dx) )

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