import sys
	
input = sys.stdin.readline
print = sys.stdout.write

def isSingleColor(v: list(list())):
    l = len(v)
    
    tmp = 0
    for row in v:
        tmp += sum(row)

    if tmp == 0 or tmp == l*l:
        return True
    else:
        return False

def divideVideo(v: list(list())):
    l = len(v)
    n = l // 2

    tmp = [[[1 for _ in range(n)] for _ in range(n)] for _ in range(4)]
    
    for y in range(l):
        for x in range(l):
            color = v[y][x]
            if y < n:
                # 제 2사분면
                if x < n:
                    tmp[0][y][x] = color
                # 제 1사분면
                else:
                    tmp[1][y][x-n] = color
            else:
                # 제 3사분면
                if x < n:
                    tmp[2][y-n][x] = color
                # 제 4사분면
                else:
                    tmp[3][y-n][x-n] = color

    return tmp

def recursion(v: list(list()), n: int):
    if (n == 1 or isSingleColor(v) == True):
        return str(v[0][0])

    subSquare = divideVideo(v)
    
    return f"({recursion(subSquare[0], n//2)}{recursion(subSquare[1], n//2)}{recursion(subSquare[2], n//2)}{recursion(subSquare[3], n//2)})"

N = int(input())

video = [list(map(int, input().rstrip())) for _ in range(N)]

print(f"{recursion(video, N)}\n")