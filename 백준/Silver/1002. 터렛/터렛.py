testCase = int(input())

array = []

for i in range(testCase) :
    array.append(list(map(int, input().split())))
    
for j in range(testCase) :
    x1, y1, r1, x2, y2, r2 = array[j]
    
    # 4가지 케이스로 나뉨
    distance = (x1-x2)**2+(y1-y2)**2
    radiusAdd = (r1+r2)**2
    radiusDif = (r1-r2)**2

    # 첫번째 케이스 : 서로 겹칠 때
    # 두 원 간의 거리와 반지름이 모두 같다면, 좌표는 무한히 발생함
    if (distance == 0 and radiusDif == 0) :
        print(-1)
    # 두번째 케이스 : 두 원이 두 점에서 만나는 경우
    # 두 원의 반지름 합이 두 원의 중심점 좌표 간의 거리보다 길다면 두 점에서 만남
    # 이 때 큰 원 내부에 작은 원이 들어가 있을 경우, 좌표 간의 거리가 두 반지름의 차보다 커야 함
    elif (radiusAdd > distance and radiusDif < distance):
        print(2)
    # 세번째 케이스 : 두 원이 한 점에서 만나는 경우
    # 내접 또는 외접
    elif (radiusAdd == distance or radiusDif == distance):
        print(1)
    # 네번째 케이스 : 두 원이 만나지 않는 경우
    # 두 원 간의 거리가 반지름 합보다 크거나(외부에 있을 때), 동심원인 경우
    else:
        print(0)
            
            
        
    