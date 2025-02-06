import sys

input = sys.stdin.readline

# [int] K: 입력받을 명령어의 개수 (범위(자연수): 1 ≤ K ≤ 100,000)
K = int(input())

# [list] stack: 계산할 정수를 담아두는 리스트 (값 범위: 0 <= number <= 1,000,000)
stack = []

for _ in range(K):
    order = int(input())
    
    # 1. 명령어가 0인 경우, 스택 최상단에서 요소를 하나 제거한다.
    if (order == 0):
        stack.pop()
    # 2. 0을 제외한 정수인 경우, 스택 최상단에 해당 정수를 추가한다.
    else :
        stack.append(order)

# 스택에 있는 모든 정수를 더하여 출력한다.
print(sum(stack))