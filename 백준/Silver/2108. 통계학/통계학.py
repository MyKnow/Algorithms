import sys
from collections import Counter

input = sys.stdin.readline

# [int] N: 수의 개수 (범위: 1 ≤ N ≤ 500,000)
N = int(input())

# [list(int)] numbers: 입력받은 수 저장
numbers = [int(input()) for _ in range(N)]

# 1. 산술평균 (소수점 첫째 자리 반올림)
print(round(sum(numbers) / N))

# 2. 중앙값 (정렬 후 중간값)
numbers.sort()
print(numbers[N // 2])

# 3. 최빈값 (Counter 활용)
counter = Counter(numbers)
mode_freq = counter.most_common()

# 최빈값이 여러 개라면 두 번째로 작은 값 선택
if len(mode_freq) > 1 and mode_freq[0][1] == mode_freq[1][1]:
    print(sorted([mode_freq[0][0], mode_freq[1][0]])[1])
else:
    print(mode_freq[0][0])

# 4. 범위 (최대값 - 최소값)
print(numbers[-1] - numbers[0])