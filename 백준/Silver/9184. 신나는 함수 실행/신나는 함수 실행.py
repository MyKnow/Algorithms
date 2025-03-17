# [def(int, int, int)] w
# : Function that returns result of calcuation by recursion with memoization
# 
# - Parameters
# [int] a, b, c: Integer that points to each index in the list called dp
#
# - Return
# [int]: Integer that value of dp[a][b][c]
def w(a, b, c):
    if (a <= 0 or b <= 0 or c <= 0):
        return 1

    if (a > 20 or b > 20 or c > 20):
        return w(20, 20, 20)

    # Return self when dp has pre-calculate value at now index
    if (dp[a][b][c]):
		    return dp[a][b][c]

    if (a < b < c):
        # Memoization
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    else:
        # Memoization
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

# [list(list(list(int)))] dp
# : 3-Dimensional list of integer that store results of function w
dp =  [ [ [0 for _ in range(21)] for _ in range(21) ] for _ in range(21) ]

while (True):
    # [int] a, b, c: Integer that points to each index in the list called dp
    a, b, c = map(int, input().split())

    if (a == b == c == -1):
        break

    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")