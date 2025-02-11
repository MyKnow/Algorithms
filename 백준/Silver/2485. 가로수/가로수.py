import sys

input = sys.stdin.readline

# [def(int, int) -> int] getGCD: 최대 공약수를 반환하는 함수
def getGCD(a, b):
    if (b==0):
        return a
    else:
        return getGCD(b, a%b)

# [int] N: 이미 심어져 있는 가로수의 수 (범위(자연수): 3 ≤ N ≤ 100,000)
N = int(input())

# [int] minOfDiff: 각 가로수 간의 거리 중에서 가장 짧은 간격을 저장하는 변수 (초기값: max)
minOfDiff = float('inf')

# [list(int)] listOfTrees: 각 가로수의 위치를 저장하는 리스트(길이: N)
listOfTrees = []

# [list(int)] listOfDiff: 각 가로수 간의 거리 차이를 저장하는 리스트
listOfDiff = []

for index in range(N):
    # [Int] nowTree: 현재 가로수의 위치를 저장하는 변수(범위(자연수): <= 1,000,000,000)
    nowTree = int(input())
    
    # index가 0일 땐 listOfTrees에 현재 가로수 위치를 추가만 한다.
    if (index != 0): 
        # [Int] nowDiff: 이전 가로수와 현재 가로수 간의 거리 차이
        nowDiff = nowTree - listOfTrees[-1]
        
        # index가 1일때(2번째 반복 때) nowTree와 첫번째 가로수의 거리 차이를 minOfDiff에 바로 갱신한다.
        if (index == 1):
            minOfDiff = nowDiff
        # index가 2 이상일 때, 최대 공약수를 통해서 minOfDiff를 갱신한다.
        else:
            # 1. 현재 거리차이와 최소 거리차이와의 최대 공약수를 구한다.
            gcd = getGCD(minOfDiff, nowDiff)

            # 2. 구한 최대 공약수를 minOfDiff로 지정한다.
            # (최대 공약수가 1인(서로소인) 경우가 명시되있지 않기 때문에, 항상 가능한 것으로 파악한다.)
            minOfDiff = gcd 
        
        # 3. 현재 거리 차이를 listOfDiff에 추가한다.
        listOfDiff.append(nowDiff)
            
    # 리스트에 가로수의 위치를 저장한다.
    listOfTrees.append(nowTree)

# [int] count: 새로 심어야 하는 가로수를 저장하는 변수 (초기값: 0)
count = 0

# listOfDiff를 순회하며, count를 증가시킨다.
for diff in listOfDiff:
    # diff와 minOfDiff가 동일하지 않다면 count를 증가시킨다.
    if (diff != minOfDiff):
        # diff를 minOfDiff로 나눈 몫에 1을 빼서 count에 더한다.
        # 나머지가 존재하지 않는다고 가정한다.
        count += diff//minOfDiff - 1

# count를 출력한다.
print(count)