# [def(list(int), list(int), int, int)] printSequence
# : 충족되는 조건의 수열을 출력하는 함수
# [list(bool)] isVisited: 이미 탐색한 숫자인지 확인하는 리스트 (길이: N)
# [list(int)] stack: sequence에서 DFS로 탐색 중인 값을 저장하는 스택
# [int] N: 자연수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
# [int] M: 수열의 길이 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
def printSequence (isVisited, stack, N, M):
    # 1. 스택의 길이가 수열 생성 조건이라면 출력함.
    if (len(stack) == M):
        print(" ".join(map(str, stack)))
        return
    else:
        # 2. 1부터 N+1까지 순회함.
        for index in range(1, N+1):
            # 3. 만약 이미 방문한 적 있는 수라면 Continue함.
            if (isVisited[index]):
                continue
            # 4. 방문한 적 없는 수라면 스택에 삽입함.
            stack.append(index)
            # 5. 방문했으므로 isVisited를 True로 변경.
            isVisited[index] = True
            # 6. 함수를 재귀하여 수열을 완성시킴.
            printSequence(isVisited, stack, N, M)
            # 7. 사용한 수를 스택에서 제거하여 다음 수를 넣을 준비를 함.
            stack.pop()
            # 8. isVisited를 다시 False로 변경하여 다음 조건문을 대비함.
            isVisited[index] = False
        

# [int] N: 자연수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
# [int] M: 수열의 길이 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
N, M = map(int, input().split())

# [list(bool)] isVisited: Index가 이미 탐색한 숫자인지 확인하는 리스트 (길이: N+1)
isVisited = [False] * (N + 1)

# [list(int)] stack: sequence에서 DFS로 탐색 중인 값을 저장하는 스택
stack = list()

# 초기값을 바탕으로 함수를 실행시킴.
printSequence(isVisited, stack, N, M)