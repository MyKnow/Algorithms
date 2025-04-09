import sys
	
input = sys.stdin.readline
print = sys.stdout.write

nM1 = 0
n0 = 0
nP1 = 0

# N: int
# description: size of given paper
# range: 1 ≤ N ≤ 3^7 (3^k)
N = int(input())

# paper: list[list[int]]
# description: Each value of points in given paper
# range: -1, 0, 1
# length: N*N
paper = [list(map(int, input().split())) for _ in range(N)]

# isSingleValue: def(list[list[int]]) -> bool
# description: A function that returns boolean based on wheter the values 
# in a given 2-Dimensional list are all the same value
def isSingleValue(v: list[list[int]]) -> bool:
    # firstValue: First value of list "v"
    firstValue = v[0][0]

    # Traveling the list v, return False if val is different value from the "firstValue"
    for row in v:
        for val in row:
            if val != firstValue:
                return False
    else:
        # Return True when iteration completes search to the end.
        return True

# recursion: def(list[list[int]])
# description: A recursive function that divided by 9 zones 
# a given 2-Dimensional list and update number of each values
def recursion(v: list[list[int]]):
    global nM1, n0, nP1
    # n: Number of rows in list v
    n = len(v)

    # Return first value when no longer divisible or is a single value
    if (n == 1 or isSingleValue(v) == True):
        val = v[0][0]
        if (val == -1):
            nM1 += 1
        elif (val == 0):
            n0 += 1
        else:
            nP1 += 1
        return

    tri = n//3

    top = v[:tri]
    mid = v[tri: tri*2]
    bot = v[tri*2:]

    # Recurvise call divided by 9 zones 
    recursion([row[:tri] for row in top])
    recursion([row[tri: tri*2] for row in top])
    recursion([row[tri*2:] for row in top])
    recursion([row[:tri] for row in mid])
    recursion([row[tri: tri*2] for row in mid])
    recursion([row[tri*2:] for row in mid])
    recursion([row[:tri] for row in bot])
    recursion([row[tri: tri*2] for row in bot])
    recursion([row[tri*2:] for row in bot])

    return

# Call function
recursion(paper)

# Print answer
print(f"{nM1}\n{n0}\n{nP1}\n")