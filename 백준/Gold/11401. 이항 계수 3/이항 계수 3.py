# N: int
# description: An integer that represents 
# the total number of integer to make combinations
# range: 1 ≤ N ≤ 4,000,000
#
# K: int
# description: An integer that represents count of 
# selected number to make a combination
# range: 0 ≤ K ≤ N
N, K = map(int, input().split())

# MOD: int
# description: An integer to mod each variable such as numerator, demoninator
# initial: 1,000,000,007
MOD = 1_000_000_007

# numerator: int
# description: An integer to store result of remainder 
# between "N * N-1 * ... * N-K+1" and "MOD"
# initial: 1
numerator = 1
for n in range(N - K + 1, N + 1):
    numerator *= n
    numerator %= MOD

# denominator: int
# description: To store result of remainder between K! and "MOD"
# initial: 1
denominator = 1
for k in range(1, K + 1):
    denominator *= k
    denominator %= MOD

# denominatorInv: Calculate inverse number with Ferma's little thorem
denominatorInv = pow(denominator, MOD - 2, MOD)

# Get result and print it
result = numerator * denominatorInv % MOD
print(result)