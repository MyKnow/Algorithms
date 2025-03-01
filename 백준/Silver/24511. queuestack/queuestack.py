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
listWithoutStack = [B[index] for index, value in enumerate(A) if value == 0]

# [int] lenOfDiff: 리스트 B와 C의 길이 차이
lenOfDiff = len(listWithoutStack) - M

# lenOfDiff가 1 이상인 경우, 리스트 B가 C보다 짧지 않다는 것을 의미하므로 -M까지 역출력한다.
if (lenOfDiff >= 1):
    print(" ".join(map(str, listWithoutStack[-M::][::-1])))
# lenOfDiff가 0인 경우 그대로 역출력한다.
elif (lenOfDiff == 0):
    print(" ".join(map(str, listWithoutStack[::-1])))
# lenOfDiff가 음수인 경우, 리스트 B가 M보다 짧다는 것을 의미하므로, 리스트 B를 역으로 출력하고
# lenOfDiff만큼 리스트 C를 정방향 출력한다.
else:
    print(" ".join(map(str, listWithoutStack[::-1]+C[:abs(lenOfDiff)])))