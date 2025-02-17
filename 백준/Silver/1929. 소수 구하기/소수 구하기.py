# [def(int)->bool] isPrimeNumber: 주어진 정수가 소수인지 확인하는 함수
def isPrimeNumber(integer):
    # 0, 1은 소수가 아니다.
    if (integer <= 1):
        return False
    # 2, 3은 소수이다.
    elif (integer <= 3):
        return True
    
    # 2부터 자기자신 이전까지 나누어 떨어지지 않으면 소수이다.
    for number in range(2, int(integer**0.5)+1):
        # 나누어 떨어지는 경우가 있으므로 즉시 False 반환
        if (integer % number == 0):
            return False
    
    return True

# [int] M, N: 소수를 찾을 정수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 1,000,000)
M, N = map(int, input().split())

for n in range(M, N+1):
    if (isPrimeNumber(n)):
        print(n)