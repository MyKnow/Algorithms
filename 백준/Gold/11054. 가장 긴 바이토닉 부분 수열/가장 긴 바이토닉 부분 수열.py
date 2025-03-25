N = int(input())

Ai = list(map(int, input().split()))

dp = [1] * N
reverseDP = [1] * N

for i in range(N):
    for j in range(i):
        if (Ai[i] > Ai[j]):
            dp[i] = max(dp[i], dp[j]+1)


Ai.reverse()
for i in range(N):
    for j in range(i):
        if (Ai[i] > Ai[j]):
            reverseDP[i] = max(reverseDP[i], reverseDP[j]+1)

reverseDP.reverse()

print(max(map(sum, zip(dp, reverseDP)))-1)