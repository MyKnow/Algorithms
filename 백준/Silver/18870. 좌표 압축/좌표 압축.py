import sys

# [list(int)] listOfPoints: 입력 받은 좌표를 저장하는 리스트 (길이: N)
listOfPoints = list(map(int, sys.stdin.read().split()[1:]))

# [list(int)] listWithoutDuplicate: 중복을 제거하여 정렬한 리스트 (길이: <= N)
listWithoutDuplicate = sorted(list(set(listOfPoints)))

# [dict(int)] dictOfPoints: 입력 받은 좌표를 압축한 사전 (길이: len(listWithoutDuplicate))
dictOfPoints = { listWithoutDuplicate[index] : index for index in range(len(listWithoutDuplicate)) }

# number를 dictOfPoints에서 찾아내어 출력한다.
for number in listOfPoints:
    print(dictOfPoints[number], end = " ")
    