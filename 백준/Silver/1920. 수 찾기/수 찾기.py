# 최대 길이가 10만인 A 수열의 내부에, 최대 길이 10만인 S의 각 요소가 존재하는 지 여부를 확인하면 된다.

N = int(input())
A = list(map(int, input().split()))

M = int(input())
S = list(map(int, input().split()))

# 1. set으로 풀기
# 간단히 A를 set으로 만들고, S를 순회하며 존재하는 지 여부만 판단하면 된다.
def solution_1():
    result = []
    setA = set(A)
    for s in S:
        if s in setA:
            result.append("1")
        else:
            result.append("0")
    return result

# 2. 이진 탐색으로 풀기
# A를 정렬한 후, 이진 탐색으로 검색을 진행한다.
def solution_2():
    A.sort()
    
    def binary_search(target):
        left, right = 0, len(A) -1
    
        while left <= right:
            mid = (left+right) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    result = []
    for s in S:
        if binary_search(s) != -1:
            result.append("1")
        else:
            result.append("0")
    return result

print("\n".join(solution_1()))
