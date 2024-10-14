# 0 <= H <= 23, 0H와 같이 불필요한 0은 생략
# 0 <= M <= 59, 0M와 같이 불필요한 0은 생략
H, M = map(int, input().split())

# 계산을 위해 조정 값 선언 및 0으로 초기화
calcH = 0
calcM = 0

# 분 계산
if (M < 45) :
    calcM = 60 + M - 45
    calcH = -1
else :
    calcM = M - 45
    
# 시간 조정이 필요한 경우
if (calcH == -1) :
    # 날짜가 조정되는 경우
    if (H == 0) :
        calcH = 23
    # 1시간 - 되는 경우
    else :
        calcH += H
# 시간 조정이 필요없는 경우
else :
    calcH = H
    
print(str(calcH) + " " + str(calcM))