# [def(int)] solution
# 퀸을 조건에 맞게 배치하는 방법의 수를 업데이트 하는 함수
# [int] row: 현재 탐색 중인 행 번호 및 퀸의 개수
def solution(row):
    global count, N
    size = len(bRow)

    # 모든 행에 퀸을 배치 완료하면 count 증가
    if row == size:  
        count += 1
        return
    
    for col in range(size):
        if not bRow[col] and not bLT2RD[col + row] and not bLD2RT[(size - 1) + (row - col)]:
            # 퀸 배치
            bRow[col] = True
            bLT2RD[col + row] = True
            bLD2RT[(size - 1) + (row - col)] = True

            # 다음 행 재귀 호출
            solution(row + 1)

            # 백트래킹 (원래 상태로 복구)
            bRow[col] = False
            bLT2RD[col + row] = False
            bLD2RT[(size - 1) + (row - col)] = False

# [int] N: 정사각형 체스판의 길이와 퀸의 개수 (범위(자연수): 1 ≤ N ≤ 15)
N = int(input())

# [list(bool))] bRow: 정사각형 맵을 선형화한 리스트
# 길이: N, 초기값: False (점유한 퀸 없음)
bRow = [False for _ in range(N)]

# [list(bool)] bLT2RD: 선형화된 y = -x 대각선 리스트
# 길이: N, 초기값: False (점유한 퀸 없음)
bLT2RD = [False for _ in range(2*(N-1)+1)]

# [list(bool)] bLD2RT: 선형화된 y = x 대각선 리스트
# 길이: N, 초기값: False (점유한 퀸 없음)
bLD2RT = [False for _ in range(2*(N-1)+1)]

# [int] count: 퀸을 놓는 방법의 수 (초기값: 0)
count = 0

# 재귀 함수를 호출하여 결과를 출력한다. (초기값: 행 번호 0)
solution(0)

# 정답 출력
print(count)