from collections import deque

# [int] N, K
# N: 원을 이룬 사람들의 수
# K: 사람을 제거할 간격
# 범위(자연수): 1 <= K <= N <= 1,000
N, K = map(int, input().split())

# [deque(int)] originalDQ: 순서대로 사람이 서 있는 deque
originalDQ = deque()
for number in range(1, N+1):
    originalDQ.append(number)
    
# [list(int)] result: 제거된 사람을 저장하는 리스트
result = []

while(len(originalDQ) > 0):
    # 1. deque를 왼쪽으로 K칸 회전시킨다.
    originalDQ.rotate(-K)
    
    # 2. 회전된 deque의 첫번째 요소를 pop하여 result에 넣는다.
    result.append(originalDQ.pop())
    
# [str] resultForOutput: 출력 포맷에 맞게 수정된 result
resultForOutput = ", ".join(map(str, result))

# 출력
print(f"<{resultForOutput}>")