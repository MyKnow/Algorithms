import sys

input = sys.stdin.readline

# [def(int, int) -> int] getLCM: math.gcd 함수를 쓰지 않고 최소 공배수를 구하는 함수
def getLCM(a, b):
    # 최대공약수를 구하기 위한 변수
    remainA, remainB = a, b
    
    # 유클리드 호제법을 사용하여 최대 공약수를 구한다.
    # 더 작은 수를 큰 수에서 나눈 나머지로 계속 대체하면서 반복하면 GCD를 구할 수 있음
    while (remainA%remainB != 0):
        remainA, remainB = remainB, remainA % remainB
        
    # remainB에 남아있는 값이 GCD임.
    # 이후 원본 a, b를 곱한 값에 GCD를 나눈 몫이 LCM이 됨.
    return (a*b) // remainB


# [int] T: 테스트 케이스의 개수 (범위(자연수): 1 ≤ T ≤ 1,000)
T = int(input())

# 테스트 케이스의 개수만큼 수행
for _ in range(T):
    # [int] A, B: 최소 공배수를 구하고자 하는 두 자연수 (범위(자연수): 1 ≤ A, B ≤ 45,000)
    A, B = map(int, input().split())
    
    print(getLCM(A, B))