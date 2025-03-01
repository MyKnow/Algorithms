# [def(int) -> int] factorial: 주어진 정수의 팩토리얼을 계산하여 반환하는 함수
def factorial(target):
    temp = 1
    
    for n in range(1, target+1):
        temp *= n
        
    return temp

# [int] N, K: 이항 계수를 구하기 위한 자연수와 정수 
# K 범위: 0 <= K <= N
# N 범위: 1 <= N <= 10
N, K = map(int, input().split())

# 이항계수 == nCk
# 즉, n개에서 k를 뽑는 조합의 개수를 의미한다.
# 공식에 따라서 n-k!를 구하고 k!와 곱한 다음, 이를 n!과 나눈 결과를 반환하면 된다.
print(factorial(N) // (factorial(N-K) * factorial(K)))