# [list(int)] listOfAngles: 각도들을 저장하는 리스트 (길이: 3)
listOfAngles = []

for _ in range(3):
    listOfAngles.append(int(input()))

# 세 각이 모두 60인 경우 정삼각형
if (all(60 == angle for angle in listOfAngles)):
    print("Equilateral")
# 세 각의 합이 180이 아닌 경우 에러
elif (sum(listOfAngles) != 180):
    print("Error")
else:
    # 같은 각이 없는 경우 부등변 삼각형
    if (listOfAngles[0] != listOfAngles[1] and listOfAngles[0] != listOfAngles[2] and listOfAngles[1] != listOfAngles[2]):
        print("Scalene")
    # 그 이외는 모두 이등변 삼각형
    else :
        print("Isosceles")