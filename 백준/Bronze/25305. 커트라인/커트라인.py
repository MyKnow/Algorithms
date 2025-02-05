# [int] N, k: 응시자의 수와 상을 받는 사람의 수 (범위(자연수): 1 <= k <= N <= 1,000)
N, k = map(int, input().split())

# [list(int)] listOfPoints: N개의 점수들을 저장하는 리스트 (길이: N)
listOfPoints = list(map(int, input().split()))

# 리스트를 내림차순 정렬하고, k-1번째 점수를 출력한다.
print(sorted(listOfPoints, reverse = True)[k-1])