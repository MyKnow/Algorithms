# [def(int, int) -> int] getGCD: 두 자연수를 입력 받아서 최대 공약수를 반환하는 함수
def getGCD(a, b):
    if (b==0):
        return a
    else:
        return getGCD(b, a%b)

# [def(int, int) -> int] getLCM: 두 자연수를 입력 받아서 최소 공배수를 반환하는 함수
def getLCM(a, b):
    return (a*b) // getGCD(a, b)

# [int] A, B: 최소 공배수를 계산할 두 정수 (범위(정수): < 100,000,000)
A, B = map(int, input().split())

# getLCM 함수를 통해서 답 출력
print(getLCM(A, B))