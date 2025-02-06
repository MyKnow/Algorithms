import sys

input = sys.stdin.readline

# [int] N, M: 두 집합 A, B의 원소의 개수 (범위: < 200,000)
N, M = map(int, input().split())

# [set(int)] A: 입력 받은 숫자를 저장하는 집합 (값: < 100,000,000)
A = set(map(int, input().split()))

# [set(int)] B: 입력 받은 숫자를 저장하는 집합 (값: < 100,000,000)
B = set(map(int, input().split()))

# 답 출력
print(len(A-B) + len(B-A))