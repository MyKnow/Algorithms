# [int] N : 마름모의 대각선 길이 / 2 + 1
N = int(input())

# 위쪽 부분 출력 (중앙 포함)
for i in range(N):
    # 공백 출력
    print(" " * (N - i - 1), end="")
    # 별 출력
    print("*" * (2 * i + 1))

# 아래쪽 부분 출력
for j in range(N - 1):
    # 공백 출력
    print(" " * (j + 1), end="")
    # 별 출력
    print("*" * (2 * (N - j - 2) + 1))