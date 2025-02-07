import sys
from collections import deque

input = sys.stdin.readline

# [int] N: 제일 아래에 있는 카드 번호 (범위(자연수): 1 <= N <= 500,000)
N = int(input())

# [deque(int)] cardStack: 1부터 N까지 오름차순으로 정리된 카드덱 (길이: N)
cardStack = deque( [i for i in range(1, N+1)] )

while (len(cardStack) > 2):
    # 1. 카드 최상단을 버린다.
    cardStack.popleft()
    
    # 2. 1번을 수행한 덱에서, 최상단에 있는 카드를 제일 아래로 옮긴다.
    cardStack.append( cardStack.popleft() )
    
# 만약 카드덱 길이가 1이라면, 첫번째 요소를, 2라면 마지막 요소를 출력한다.
print(cardStack[0] if len(cardStack) == 1 else cardStack[1])