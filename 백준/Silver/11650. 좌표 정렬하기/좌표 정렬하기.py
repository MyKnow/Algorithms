# [int] N: 입력 받을 점의 개수 (범위(정수): 1 <= N <= 100,000)
N = int(input())

# [list(tuple(int, int))] listOfPoints: 입력 받은 좌표를 저장하는 리스트 (길이: N)
listOfPoints = []

for _ in range(N):
    listOfPoints.append(tuple(map(int, input().split())))
    
# [list(tuple(int, int))] sortedList: tuple의 좌표를 기준으로 오름차순 정렬한 배열
sortedListByX = sorted(listOfPoints, key = lambda x: (x[0], x[1]))

for x, y in sortedListByX:
    print(f"{x} {y}")