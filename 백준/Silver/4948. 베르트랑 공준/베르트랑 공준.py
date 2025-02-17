import sys

input = sys.stdin.readline

# [def(int)->list(int)] getPrimeNumberList: 주어진 int까지의 소수가 담긴 리스트를 반환하는 함수
def getPrimeNumberList(integer): 
    # [list(bool)] primeList: 0부터 integer까지의 index를 가지고 있는 리스트 (초기값: True)
    primeList = [True for _ in range(integer+1)]
    
    # [int] sqrtInt: integer의 제곱근
    sqrtInt = int(integer ** 0.5)
    
    # 2부터 sqrtInt+1까지 primeList를 업데이트함.
    for n in range(2, sqrtInt+1):
        # n이 소수면 n의 배수는 소수가 아님.
        if (primeList[n]):
            # n의 배수들을 모두 False로 설정 (n * n부터 시작)
            for i in range(n * n, integer + 1, n):
                primeList[i] = False
    # primeList에서 index가 integer//2보다 크며, 값이 True인 index만 모아서 정수 리스트로 반환한다.
    # [list(int)] result: 위 조건에 맞는 값을 저장하는 리스트
    result = [index for index in range(integer//2+1, integer + 1) if primeList[index]]
    
    return result

# [int] n: 소수의 개수를 구하기 위한 범위 (범위(자연수): 1 ≤ n ≤ 123,456)
while True:
    n = int(input())

    if (n == 0):
        break
        
    print(len(getPrimeNumberList(n*2)))