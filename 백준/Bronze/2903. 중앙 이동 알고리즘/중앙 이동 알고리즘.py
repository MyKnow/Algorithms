# [int] N: 중앙 이동 알고리즘을 적용하는 횟수 (범위 : 1 <= N <= 15)
N = int(input())

# 과정을 거듭할 때마다 한 변의 사각형의 개수는 2배씩 늘어남
# 1, 2, 4, 8, ..., 2^n
# [int] squreOfSide: 한 변의 사각형 개수
squresOfSide = pow(2, N)

# 한 변을 구성하는 점의 개수는 사각형의 점 개수 + 1
# [int] pointsOfSide: 한 변의 점의 개수
pointsOfSide = squresOfSide + 1

# 점의 총 개수는  pointsOfSide의 제곱
print(pointsOfSide**2)