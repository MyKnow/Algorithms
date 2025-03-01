import math

# [int] T: 테스트 케이스의 개수
T = int(input())

for _ in range(T):
    # [int] N, M: 강의 서쪽 사이트와 동쪽 사이트의 개수 (범위(정수): 0 < N ≤ M < 30)
    N, M = map(int, input().split())

    print(math.factorial(M) // (math.factorial(M-N) * math.factorial(N)))