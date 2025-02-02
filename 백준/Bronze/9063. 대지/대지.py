#[int] N: 좌표의 개수 (범위: 1 <= N <= 100,000)
N = int(input())
    
# [int] min_x, min_y, max_x, max_y : 좌하단과 우상단 좌표를 저장하는 튜플
# 각 변수의 초기값은 의도에 맞게 입력 범위의 최대값, 최소값으로 초기화한다.
min_x, min_y = 10000, 10000
max_x, max_y = -10000, -10000

for _ in range(N):
    # [int] x, y: 입력 받은 좌표 (범위(정수): -10,000 <= x, y <= 10,000)
    x, y = map(int, input().split())
    
    # 각 좌표를 조건에 맞게 변경해나간다.
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    
# 좌하단, 우상단 좌표를 통해 넓이 계산 및 출력
print((max_x - min_x) * (max_y - min_y))