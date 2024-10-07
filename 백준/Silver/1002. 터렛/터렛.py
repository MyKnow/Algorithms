testCase = int(input())

array = []

for i in range(testCase) :
    array.append(list(map(int, input().split())))
    
for j in range(testCase) :
    x1, y1, r1, x2, y2, r2 = array[j]
    
    # 존재 가능 좌표의 수가 무한인 경우 == 터렛 둘의 좌표와 감지된 거리가 모두 동일할 때
    if (x1 == x2 and y1 == y2 and r1 == r2) :
        print(-1)
    # 나머지 경우엔 3가지 케이스로 나뉨
    else :
        distance = (x1-x2)**2+(y1-y2)**2
        radiusAdd = (r1+r2)**2
        radiusDif = (r1-r2)**2
        
        # 첫번째 케이스 : 두 원이 두 점에서 만나는 경우
        # 두 원의 반지름 합이 두 원의 중심점 좌표 간의 거리보다 길다면 두 점에서 만남
        # 이 때 큰 원 내부에 작은 원이 들어가 있을 경우, 좌표 간의 거리가 두 반지름의 차보다 커야 함
        if (radiusAdd > distance and radiusDif < distance):
            print(2)
        # 두번째 케이스 : 두 원이 한 점에서 만나는 경우
        # 내접 또는 외접
        elif (radiusAdd == distance or radiusDif == distance):
            print(1)
        # 세번째 케이스 : 두 원이 만나지 않는 경우
        # 두 원 간의 거리가 반지름 합보다 크거나(외부에 있을 때), 동심원인 경우
        elif (radiusAdd < distance or radiusDif > distance or (distance == 0 and r1 != r2)):
            print(0)
            
            
        
    