# [list(int)] listOfPiece : 동혁이가 찾은 흰색 체스 기물 개수 리스트 (0 <= int <= 10)
listOfPiece = list(map(int, input().split()))

# 체스 기물 중에서
# 킹과 퀸은 1개
# 룩, 비숍, 나이트는 2개
# 폰은 8개
# 이므로, 순서에 따라 조건을 다르게 검사한다.
for index in range(len(listOfPiece)) :
    # [int] numberOfRequired: 필요한 기물 수 (초기 값은 킹, 퀸, 폰을 제외한 각 기물의 필요 기물 수)
    numberOfRequired = 2
    
    # 킹 또는 퀸일 떄
    if (index == 0 or index == 1) :
        numberOfRequired = 1
    # 폰일 때
    elif (index == len(listOfPiece)-1) :
        numberOfRequired = 8

    # 필요 기물 수에서 현재 index의 기물 수를 뺀 수를 출력한다.
    print(numberOfRequired - listOfPiece[index], end=" ")