# [tuple(str, str)] inputOfProblem: 문제의 입력을 분리한 튜플
inputOfProblem = input().split()

# [str] N : B진법 수 
N, _ = inputOfProblem

# [int] B: 진법 수 (2 <= B <= 36)
_, B = inputOfProblem
B = int(B)

# [int] sumOfN: 10진법으로 변환한 N (10진법으로 변환한 크기: <=100,000,000)
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35 진법
sumOfN = 0

# 문자열 N을 순회하며 계산
for i in range(len(N)):
    # [str] n: N 문자열의 앞에서 i번째 문자
    n = N[i]
    
    # 문자인 경우 변환 필요
    if ('A' <= n <= 'Z'):
        # (변환된 수) * (진법**자리)
        sumOfN += int(ord(n)-ord('A')+10) * (B**(len(N)-i-1))
    else :
        sumOfN += int(n) * (B**(len(N)-i-1))

# 출력
print(sumOfN)