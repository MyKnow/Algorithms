import sys

input = sys.stdin.readline

# [int] N: 자료구조의 개수 (범위(자연수): 1 ≤ N ≤ 100,000)
N = int(input())

# [list(int)] A: 각 자리의 자료구조의 형태를 나타내는 수열 (0: 큐, 1: 스택, 길이: N)
A = list(map(int, input().split()))

# [list(int)] B: 각 자리의 자료구조의 초기값 (길이: N, 범위(자연수): 1 ≤ B_i ≤ 1,000,000,000)
B = list(map(int, input().split()))

# [int] M: 삽입할 수열의 길이 (범위(자연수): 1 ≤ M ≤ 100,000)
M = int(input())

# [list(int)] C: queuestack에 삽입할 원소를 담은 길이 M의 수열 (길이: M, 범위(자연수): 1 ≤ C_i ≤ 1,000,000,000)
C = list(map(int, input().split()))

# [list(int)] listWithoutStack: Stack 부분이 제외된 수열 B를 나타내는 리스트
listWithoutStack = [B[index] for index in range(N) if A[index] == 0]

# 항상 역출력 하므로 미리 뒤집는다.
listWithoutStack.reverse()

# 두 리스트를 합친 다음, 길이 M만큼 출력한다.
print(" ".join(map(str, (listWithoutStack+C)[:M])))