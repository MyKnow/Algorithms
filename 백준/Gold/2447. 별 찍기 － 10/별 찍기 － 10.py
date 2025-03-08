# [def(list(list(str)), int, (int, int), (int, int) -> list(list(str))] makeStar
# 3^k 길이를 가진 별 모양 패턴을 반환하는 함수
# [list(list(str))] k: 변경할 이중 리스트
# [int] level: 현재 재귀 레벨
# [int] startX:  작업을 진행할 범위 중 좌상단의 X 좌표
# [int] startY:  작업을 진행할 범위 중 좌상단의 Y 좌표
def makeStar(k, level, startX, startY):
    # 1. level이 1인 경우 더 이상 공백을 뚫을 수 없으므로 종료함.
    if (level == 1):
        return

    # [int] subLen: 현재 정사각형의 한 변을 3분할한 길이
    subLen = level // 3
    
    # 2. 현재 정사각형에서 start와 end 좌표를 참고하여 구멍을 뚫는다.
    for x in range(startX+subLen, startX+subLen*2):
        for y in range(startY+subLen, startY+subLen*2):
            k[y][x] = " "
            
    # 4. 구멍을 뚫은 정사각형의 나머지 8개 부분에 대하여 재귀적으로 구멍을 뚫는다.
    for x in range(3):
        for y in range(3):
            if not (x == 1 and y == 1):
                makeStar(k, subLen, startX + subLen*x, startY + subLen*y)
            

# [Int] N: 정사각형 모양의 재귀적인 별 패턴을 생성할 크기 (범위: 3^K -> 1 <= K < 8)
N = int(input())

# [list(list(str))] square: 공백을 뚫을 사각형을 표현하는 이중 리스트 (길이: N*N)
square = [["*" for _ in range(N)] for _ in range(N)]

# square에 규칙대로 구멍을 뚫는다.
makeStar(square, N, 0, 0)

# square를 출력한다.
for row in square:
    print("".join(row))