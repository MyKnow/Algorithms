import sys
from collections import deque

input = sys.stdin.readline

# [int] N: 주어진 명령의 수 (범위: 1 ≤ N ≤ 2,000,000)
N = int(input().strip())

# [deque[int]] queue: 정수를 저장하는 큐
queue = deque()

# [list[int]] result: 출력할 결과를 저장하는 리스트
result = []

for _ in range(N):
    order = input().strip()
    
    # 1. push X: 정수 X를 queue에 넣는 연산
    if order.startswith("push"):
        _, X = order.split()
        queue.append(int(X))
    # 2. pop: queue의 가장 앞에 있는 정수를 빼서 출력하는 연산
    elif order == "pop":
        result.append(queue.popleft() if queue else -1)
    # 3. size: queue에 들어있는 정수 개수 출력
    elif order == "size":
        result.append(len(queue))
    # 4. empty: 큐가 비어있으면 1, 아니면 0 출력
    elif order == "empty":
        result.append(1 if not queue else 0)
    # 5. front: 큐의 가장 앞 정수를 출력, 없으면 -1
    elif order == "front":
        result.append(queue[0] if queue else -1)
    # 6. back: 큐의 가장 뒤 정수를 출력, 없으면 -1
    elif order == "back":
        result.append(queue[-1] if queue else -1)

# 최종 결과 출력
sys.stdout.write("\n".join(map(str, result)) + "\n")