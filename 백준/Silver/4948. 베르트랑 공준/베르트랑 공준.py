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
    # primeList에서 index가 2보다 크거나 같으며, 값이 True인 index만 모아서 정수 리스트로 반환한다.
    # [list(int)] result: 위 조건에 맞는 값을 저장하는 리스트
    result = [index for index in range(2, integer + 1) if primeList[index]]
    
    return result

# [def(list(int), int) -> int] binarySearch: 리스트에서 목표 값의 위치를 반환하는 함수
def binarySearch(data, target):
    # 1. data는 이미 정렬되어 있으므로, 정렬 과정 생략.
    
    # 2. left, right 선언
    left = 0
    right = len(data) - 1
    
    # 3. left가 right보다 커지면 종료
    while (left <= right):
        # 4. mid 선언
        mid = (left+right)//2
        
        # 5. mid가 target보다 크다면 right를 mid-1로 업데이트
        if (data[mid] > target):
            right = mid - 1
        # 6. mid가 target보다 작거나 같다면 left를 mid+1로 업데이트
        else:
            left = mid + 1
            
    # 8. left 출력
    return left

# [list(int)] listOfPrimeNumbers: 123,456 * 2보다 작은 소수들을 저장한 리스트
listOfPrimeNumbers = getPrimeNumberList(123456 * 2)

# [int] n: 소수의 개수를 구하기 위한 범위 (범위(자연수): 1 ≤ n ≤ 123,456)
while True:
    n = int(input())

    if (n == 0):
        break
        
    print(binarySearch(listOfPrimeNumbers, n*2)-binarySearch(listOfPrimeNumbers, n))