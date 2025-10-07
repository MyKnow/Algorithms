# * 요약
# - 2x2 형태로 4개가 붙어있을 경우 사라지면서, 사라진 블록 수만큼 점수를 얻는다.
# - 블록이 사라지면, 해당 자리로 위에 있는 블록이 떨어지며 빈 공간을 채운다.
# - 빈 공간을 채운 후에 다시 2x2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복한다.

# * 입력
# - m, n: 게임판의 세로, 가로 길이 (2 ≦ n, m ≦ 30)
# - board: 게임판, 길이 n인 문자열 m개의 배열 (알파벳 대문자 Only)
#
# * 출력
# - 지워진 블록 수

def solution(m, n, board):
    # 편의를 위해 board를 이중 배열로 변환한다.
    board = [list(row) for row in board]
    
    # (좌상단 생략), 우상단, 좌하단, 우하단
    coords = [ (0, 1), (1, 0), (1, 1) ]
    
    total_count = 0
    while True:
        # 1. 매 턴마다 board를 2x2 형태로 스캔하며, 지울 수 있는 공간의 좌상단 좌표를 기록해둔다.
        # 바로 지우지 않는 이유는, 스캔 구역 일부가 겹치는 경우를 대비하기 위함이다.
        found_coords = []
        for y in range(m-1):
            for x in range(n-1):
                # lu: 좌상단 타일 값
                lu = board[y][x]
                
                # 좌상단 타일이 비어있다면 넘긴다.
                if lu == "":
                    continue
                    
                # 하나라도 다른 타일이 있다면 넘어간다.
                for dx, dy in coords:
                    if lu != board[y+dy][x+dx]:
                        break
                else:
                    # 모든 타일이 동일한 캐릭터라면 좌상단 좌표를 기록한다.
                    found_coords.append( (x, y) )
                    
        # ! 제거할 블록이 없다면 반복문을 종료한다.
        if not found_coords:
            break
        
        # 2. found_coords에서 좌상단 좌표를 다시 꺼내어, 제거할 부분의 타일 값을 "-"로 치환하고 "-"의 총 갯수를 센다.
        # 공백으로 치환하지 않는 이유는 제거한 타일의 수만을 세기 위함이다.
        for x, y in found_coords:
            for dx, dy in [(0, 0)] + coords:
                board[dy+y][dx+x] = "-"
            
        # 3. "-"의 수를 셈과 동시에 제거한다.
        for y in range(m):
            for x in range(n):
                if board[y][x] == "-":
                    board[y][x] = ""
                    total_count += 1
        
        # 4. 리스트의 각 열에서 공백을 제거한 새로운 열을 생성한 뒤
        # 공백이 상단에 가게끔 정렬하여 board를 업데이트한다.
        for x in range(n):
            new_col = [board[y][x] for y in range(m) if board[y][x] != ""]
            new_col = [""]*(m - len(new_col)) + new_col
            for y in range(m):
                board[y][x] = new_col[y]

    return total_count