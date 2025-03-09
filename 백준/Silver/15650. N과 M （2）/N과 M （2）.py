# [def(list(bool), list(int), int, int)] printSequence
# : 주어진 조건에 맞는 수열을 집합에 저장하는 함수
# [set(tuple(int))] setOfSequence: 조건에 맞는 수열을 저장하는 집합
# [list(bool)] isVisited: 방문한 적 있는 인덱스를 저장하는 리스트 (길이: N)
# [list(int)] stack: 현재 DFS로 탐색 중인 수를 저장하는 리스트
# [int] N: 자연수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
# [int] M: 수열의 길이 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
def printSequence(setOfSequence, isVisited, stack, N, M):
    # 1. 만약 스택의 길이가 M과 같다면 집합에 저장한다.
    # 이 때 stack을 정렬하고 tuple로 변환하여, 중복값을 저장하지 못하도록 한다.
    if (len(stack) == M):
        setOfSequence.add(tuple(sorted(stack)))
        return
    # 2. 1부터 N+1까지 DFS를 진행한다.
    for index in range(1, N+1):
        # 3. 만약 현재 index를 방문한 적이 있다면 넘어간다.
        if (isVisited[index]):
            continue
        # 4. 방문한 적 없는 index라면 스택에 넣고 방문처리 한다.
        stack.append(index)
        isVisited[index] = True
        # 5. 조건에 충족한 수열을 찾을 때까지 재귀적으로 호출한다.
        printSequence(setOfSequence, isVisited, stack, N, M)
        # 6. 수열을 모두 생성하였으므로 stack에서 제거하고 방문처리를 해제한다.
        stack.pop()
        isVisited[index] = False
        

# [int] N: 자연수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
# [int] M: 수열의 길이 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
N, M = map(int, input().split())

# [list(bool)] isVisited: 방문한 적 있는 인덱스를 저장하는 리스트 (길이: N)
isVisited = [False] * (N+1)

# [list(int)] stack: 현재 DFS로 탐색 중인 수를 저장하는 리스트
stack = list()

# [set(tuple(int))] setOfSequence: 조건에 맞는 수열을 저장하는 집합
setOfSequence = set()

# DFS로 탐색하여 조건에 맞는 수열을 집합에 저장한다.
printSequence(setOfSequence, isVisited, stack, N, M)

# 집합에 저장된 값을 정렬하여 출력한다.
for s in sorted(list(setOfSequence)):
    print(" ".join(map(str, s)))