# [int] N: An integer that represents number of digits
N = int(input())

# [list(list(int))] dp: 2-Dimensional list that store number of cases at each digits 
dp = [[0] + [1] * 9 for _ in range(N)]

for idx in range(1, N):
    # 0 is only possible if the previous number is 1
    dp[idx][0] = dp[idx-1][1]
    # 9 is only possible if the previous number is 8
    dp[idx][9] = dp[idx-1][8]

    for number in range(1, 9):
        dp[idx][number] = (dp[idx-1][number-1] + dp[idx-1][number+1])

print(sum(dp[N-1]) % 1_000_000_000)