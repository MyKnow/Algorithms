while(True):
    # [(int, int)] n1, n2: 약수와 배수 관계를 계산할 두 자연수 (범위: 0 < n < 10,000)
    n1, n2 = map(int, input().split())
    
    # n1, n2 둘 다 0인 경우 종료한다.
    if (n1 == n2 == 0) :
        break
    
    # 첫 번째 숫자가 두 번째 숫자의 약수인 경우.
    if (n2 % n1 == 0):
        print("factor")
    # 첫 번째 숫자가 두 번째 숫자의 배수인 경우.
    elif (n1 % n2 == 0):
        print("multiple")
    # 둘 다 아니라면
    else :
        print("neither")