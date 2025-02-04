# [int] N, M: 보드의 세로, 가로 길이 (범위(자연수): 8 <= N, M <= 50))
N, M = map(int, input().split())

# [list(list(str))] board: 입력받은 N, M 크기의 보드판을 입력 받기 위한 이중 리스트 (길이: N*M)
board = [list(input()) for _ in range(N)]

# [float] minOfFixCount: 보드판을 칠해야 하는 정사각형 최소 개수 (초기값: N*M (모든 칸이 오류))
minOfFixCount = N*M

# index를 넘어가지 않도록 처리함.
for n in range(N-8+1):
    for m in range(M-8+1):
        # [int] sumOfFix_W, sumOfFix_B: 다시 칠해야 하는 정사각형 개수를 저장하는 변수
        sumOfFix_W = 0  # 'W'로 시작하는 체스판
        sumOfFix_B = 0  # 'B'로 시작하는 체스판
        
        for y in range(8):
            for x in range(8):
                nowColor = board[y+n][x+m]
                
                # 'W'로 시작하는 경우
                if ((x + y) % 2 == 0):  # 짝수 위치
                    if nowColor != "W":
                        sumOfFix_W += 1
                    if nowColor != "B":
                        sumOfFix_B += 1
                else:  # 홀수 위치
                    if nowColor != "B":
                        sumOfFix_W += 1
                    if nowColor != "W":
                        sumOfFix_B += 1
        
        # 리스트에 sumOfFix를 추가함.
        minOfFixCount = min(minOfFixCount, sumOfFix_W, sumOfFix_B)
        
# 모든 보드판을 탐색하여 countOfFix에 고쳐야 할 보드칸 개수가 저장되면, 그 중 최소값을 출력한다.
print(minOfFixCount)