# [list(int)] listOfX: 등장한 x 좌표를 저장하는 list  
listOfX = []
# [list(int)] listOfY: 등장한 y 좌표를 저장하는 list
listOfY = []

# 직사각형의 세 꼭짓점 좌표를 입력 받는다.
for _ in range(3):
    # [int] x, y: 각 꼭짓점의 x, y 좌표 (범위(자연수): 1 <= x, y <= 1,000)
    x, y = map(int, input().split())
    
    # 각 좌표에서 가장 적게 등장한 값이 찾고자 하는 점의 좌표이다.
    # 이미 각 리스트에 해당 값이 들어있으면 삭제하고, 없으면 추가한다.
    if (x in listOfX):
        listOfX.remove(x)
    else :
        listOfX.append(x)
    
    if (y in listOfY):
        listOfY.remove(y)
    else :
        listOfY.append(y)

# 각 list의 첫번째 값을 출력한다.
print(f"{listOfX[0]} {listOfY[0]}")