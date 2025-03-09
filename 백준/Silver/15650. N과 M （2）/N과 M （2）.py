# [def(list(tuple(int)), list(int), int, int, int)] printSequence
# : 주어진 조건에 맞는 수열을 집합에 저장하는 함수
# [list(tuple(int))] results: 조건에 맞는 수열을 저장하는 리스트
# [list(int)] stack: 현재 DFS로 탐색 중인 수를 저장하는 리스트
# [int] N: 자연수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
# [int] M: 수열의 길이 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
# [int] start: DFS를 시작할 시작 index
def printSequence(results, stack, N, M, start):
    # 1. 만약 스택의 길이가 M과 같다면 리스트에 저장한다.
    if (len(stack) == M):
        results.append(tuple(stack))
        return
    # 2. 1부터 N+1까지 DFS를 진행한다.
    for index in range(start, N+1):
        # 3. 현재 index를 스택에 넣는다.
        stack.append(index)
        # 4. 현재 index 이후의 수로만 재귀적으로 호출한다.
        printSequence(results, stack, N, M, index+1)
        # 5. 스택에서 현재 index를 제거한다.
        stack.pop()
        
# [int] N: 자연수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
# [int] M: 수열의 길이 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
N, M = map(int, input().split())

# [list(tuple(int))] setOfSequence: 조건에 맞는 수열을 저장하는 집합
results = list()

# DFS로 탐색하여 조건에 맞는 수열을 리스트에 저장한다.
printSequence(results, [], N, M, 1)

# 집합에 저장된 값을 정렬하여 출력한다.
for s in results:
    print(" ".join(map(str, s)))