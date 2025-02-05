# [int] N: 입력 받을 좌표의 개수 (범위(정수): 1 ≤ N ≤ 100,000)
N = int(input())

# [list(tuple(int, int))] listOfPoints 입력 받은 좌표를 저장하는 리스트 (길이: N)
listOfPoints = [ tuple(map(int, input().split())) for _ in range(N) ]

# 리스트를 y좌표 우선으로 정렬한다.
listOfPoints.sort(key = lambda x: (x[1], x[0]))

# 출력
for x, y in listOfPoints:
    print(f"{x} {y}")