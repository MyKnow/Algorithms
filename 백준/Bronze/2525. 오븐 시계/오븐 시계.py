# 현재 시각 A시 B분
# 0 <= A <= 23, 10의 자리에 오는 0은 생략
# 0 <= B <= 59, 10의 자리에 오는 0은 생략
A, B = map(int, input().split())

# 요리하는 데 필요한 시간 C분
# 0 <= C <= 1,000
C = int(input())

# 시간 조정에 필요한 변수 선언 및 초기화
# calcM : B와 C를 더한 후 나머지 계산 == 계산된 분
calcM = (B + C) % 60
# calcH : B와 C를 더한 후 60으로 나눈 몫 계산 == 초과된 시
calcH = (B + C) // 60

# 시간 조정이 필요해진 경우 == calcH가 0이 아닌 경우
if (calcH != 0) :
    # 날짜 조정이 필요한 경우 == 계산된 시간을 24로 나눈 몫이 0보다 클 경우
    if ((A+calcH) // 24 > 0) :
        # 나머지를 calcH에 저장
        calcH = ((A+calcH) % 24)
    else :
        # 날짜 조정이 필요없는 경우 바로 더함
        calcH += A
else :
    # 시간 조정이 필요없는 경우
    calcH = A

print(str(calcH) + " " + str(calcM))