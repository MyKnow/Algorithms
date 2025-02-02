#[int] N: 좌표의 개수 (범위: 1 <= N <= 100,000)
N = int(input())

# [list[tuple]] listOfPoint: 각 좌표 튜플을 저장하는 리스트 (길이: N)
listOfPoint = []

for _ in range(N):
    # 입력 받은 좌표를 리스트에 추가한다. (범위(정수): -10,000 <= point <= 10,000)
    listOfPoint.append(tuple(map(int, input().split())))
    
# [tuple(int, int)] rightTopPoint, leftBottomPoint : 좌하단과 우상단 좌표를 저장하는 튜플
# 각 튜플의 초기값은 의도에 맞게 입력 범위의 최대값, 최소값으로 초기화한다.
rightTopPoint = (-10000, -10000)
leftBottomPoint = (10000, 10000)

for x, y in listOfPoint:
    # 각 좌표를 조건에 맞게 변경해나간다.
    rightTopPoint = (max(rightTopPoint[0], x), max(rightTopPoint[1], y))
    leftBottomPoint = (min(leftBottomPoint[0], x), min(leftBottomPoint[1], y))

# 좌하단, 우상단 좌표를 통해 넓이 계산 및 출력
print((rightTopPoint[1]-leftBottomPoint[1]) * (rightTopPoint[0]-leftBottomPoint[0]))