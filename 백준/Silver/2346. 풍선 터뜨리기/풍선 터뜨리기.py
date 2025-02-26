from collections import deque

# [int] N: 풍선의 개수 (범위(자연수): 1 ≤ N ≤ 1,000)
N = int(input())

# [list(int)] balloons: N개의 풍선 속 종이의 값으로 이루어진 리스트(길이: N)
balloons = map(int, input().split())

# [deque(int, int)] dq: N개의 풍선의 (번호, 값) 튜플로 이루어진 Deque (길이: <= N)
dq = deque(enumerate(balloons, start=1))

# [list(int)] result: 풍선에서 확인된 값을 저장하는 리스트
result = []

# 풍선을 모두 터뜨릴 때까지 반복
while(len(dq) != 0):
    # [Int] index, value: 가장 좌측에 있는 풍선의 순서와 종이의 값
    index, value = dq.popleft()
    
    # 풍선의 번호를 결과에 저장함
    result.append(index)
    
    # dq 속에 요소가 남아있을 때만 진행
    if (dq) :
        # rotate 값이 양수라면 이미 popLeft에 의해 좌측 개수가 하나 빠진 상태이므로 value-1 만큼 회전 시킴
        if (value > 0):
            # rotate의 방향을 맞춰주기 위해 음수를 곱함
            dq.rotate((value-1) * -1)
        else:
            dq.rotate(value * -1)
    
    
# 값을 한 번에 출력함
print(" ".join(map(str, result)))