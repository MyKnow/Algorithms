# 시간복잡도는 O(n^2)이므로 최고차항의 차수는 2이다.
# 수행 횟수는 (n-1)! 이다.

# [int] n: 입력의 크기 (범위: 1 ≤ n ≤ 500,000)
n = int(input())

# [int] exeCount: 수행 횟수를 저장하는 변수
exeCount = 0

for i in range(n):
    exeCount += i

print(f"{exeCount}\n2")