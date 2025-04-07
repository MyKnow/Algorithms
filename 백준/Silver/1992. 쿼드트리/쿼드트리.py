import sys
	
input = sys.stdin.readline
print = sys.stdout.write

def isSingleColor(v: list[list[int]]) -> bool:
    color = v[0][0]
    for row in v:
        for val in row:
            if val != color:
                return False
    return True

def recursion(v: list(list())):
    n = len(v)
    
    if (n == 1 or isSingleColor(v) == True):
        return str(v[0][0])

    half = n//2
    return "(" + \
        recursion([row[:half] for row in v[:half]]) + \
        recursion([row[half:] for row in v[:half]]) + \
        recursion([row[:half] for row in v[half:]]) + \
        recursion([row[half:] for row in v[half:]]) + \
        ")"

N = int(input())

video = [list(map(int, input().rstrip())) for _ in range(N)]

print(f"{recursion(video)}\n")