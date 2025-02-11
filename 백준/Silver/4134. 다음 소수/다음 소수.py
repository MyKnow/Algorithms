import sys

input = sys.stdin.readline

# [def(int) -> bool] isPrime: 주어진 자연수가 소수인지 판별하는 함수
def isPrime(number):
    # 0, 1은 소수가 아님
    if (number < 2):
        return False
    # 2, 3은 소수임
    elif (number < 4):
        return True
    
    # [int] squareRoot: number의 제곱근
    squareRoot = int(number**0.5)
    
    # 2부터 number의 제곱근까지 i를 증가시켜서, number가 i로 나누어 떨어지는 지 확인함.
    for i in range(2, squareRoot+1):
        if (number % i == 0):
            return False
    else:
        return True
    

# [int] N: 테스트 케이스의 개수
N = int(input())

for _ in range(N):
    # [int] n: 본인보다 크거나 같은 소수를 찾을 기준이 되는 정수 (범위(정수): 0 <= n <= 4*10^9)
    n = int(input())
    
    while(isPrime(n) == False):
        n+=1
    
    # n을 출력한다.
    print(n)