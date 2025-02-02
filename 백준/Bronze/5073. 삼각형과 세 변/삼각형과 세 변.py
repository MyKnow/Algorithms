while True:
    # [int] s1, s2, s3: 삼각형의 세 변
    s1, s2, s3 = map(int, input().split())

    # 종료 조건 (0, 0, 0 입력 시)
    if (s1 == 0 and s2 == 0 and s3 == 0):
        break
    
    # 삼각형 조건 (삼각형 부등식 체크)
    if (s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1):
        print("Invalid")
    else:
        # [int] uniqueSides: 변의 개수에 따른 삼각형 판별을 위한 set 길이 변수
        uniqueSides = len(set([s1, s2, s3]))

        if (uniqueSides == 1):
            print("Equilateral")  # 정삼각형
        elif (uniqueSides == 2):
            print("Isosceles")  # 이등변 삼각형
        else:
            print("Scalene")  # 부등변 삼각형