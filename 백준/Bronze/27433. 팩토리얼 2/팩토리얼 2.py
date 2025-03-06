# [int] N: 팩토리얼을 찾을 정수 (범위: 0 ≤ N ≤ 12)
N = int(input())

# [int] fact: 답을 계산하는 변수
fact = 1
for n in range(1, N+1):
    fact *= n
    
print(fact)