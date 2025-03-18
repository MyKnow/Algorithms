# [def(int) -> int] solution
# function that returns the number of cases when placing n tiles
#
# - Parameters
# [int] N: Integer that represents number of tiles
#
# - Returns
# [int] result: Integer that represents number of cases
def solution(N: int):
    # [list(int)] dp: List of integers that stores number of cases when placing n tiles
    dp = [0] * (N + 1)
    dp[N] = 1
    dp[N-1] = 2

    # Repeat from the back for memory savings
    for idx in range(N-2, 0, -1):
        # Update result with each previous values.
        dp[idx] = (dp[idx+1] + dp[idx+2]) % 15746
        # Pop the last index for memory savings
        dp.pop()

    return dp[1]

# [int] N: Integer that represents number of tiles
N = int(input())

print(solution(N))