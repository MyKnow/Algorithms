import sys

input = sys.stdin.readline

# [def(int, int) -> int] getLCM: math.gcd 함수를 쓰지 않고 최소 공배수를 구하는 함수
def getLCM(a, b):
    # [int] index: 2부터 나누기 시작한다.
    index = 2
    
    # [int] gcd: 최소 공약수
    gcd = 1
    
    # a와 b의 서로소가 나올 때까지 공약수로 나눈다.
    # a, b 중에서 더 작은 수까지만 index를 증가시킨다.
    while (index <= min(a, b)):
        # index로 두 수가 모두 나눠지면, a, b, gcd를 업데이트한다.
        if (a % index == 0 and b % index == 0):
            a //= index
            b //= index
            gcd *= index
        # 나눠지지 않는다면 index를 1 증가시킨다.
        else :
            index += 1
            
    # 최대공약수에 서로소인 a, b까지 곱하면 최소 공배수가 된다.
    return gcd * a * b


# [int] T: 테스트 케이스의 개수 (범위(자연수): 1 ≤ T ≤ 1,000)
T = int(input())

# 테스트 케이스의 개수만큼 수행
for _ in range(T):
    # [int] A, B: 최소 공배수를 구하고자 하는 두 자연수 (범위(자연수): 1 ≤ A, B ≤ 45,000)
    A, B = map(int, input().split())
    
    print(getLCM(A, B))