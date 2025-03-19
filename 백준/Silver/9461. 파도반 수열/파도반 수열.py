# [def(int) -> int] P
# : A Function that returns length of nth triangle
#
# - Parameter
# [int] N: An Integer that represents index of 
# triangle to find the length of sides
#
# - Return
# [int] dp[N]: An Integer that represents length of side of nth triangle
def P(N: int):
    # import maxN for optimization
    global maxN

    # Return dp[N] if nth triangle has been calculated
    if (maxN > N):
        return dp[N]

    # Repeat maxN+1 to N+1 to reduce duplicate calculations
    for idx in range(maxN+1, N+1):
        dp[idx] = dp[idx-5] + dp[idx-1]

    # Update maxN
    if (maxN < N):
        maxN = N

    return dp[N]

# [int] T: Number of test cases
T = int(input())

# [list(int)] dp: List of integer that store lengths of side of nth triangles
dp = [0] * (101)
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

# [int] maxN: Integer that stores last calculated index
maxN = 5

for _ in range(T):
    # [int] N: An Integer that represents index of 
    # triangle to find the length of sides
    N = int(input())
    
    print(P(N))