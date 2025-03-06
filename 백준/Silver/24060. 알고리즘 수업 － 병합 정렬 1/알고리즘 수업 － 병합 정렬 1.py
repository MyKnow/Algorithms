# [def(list(int), int, int) -> int] mergeSort: 주어진 배열을 오름차순 정렬하는 함수
def mergeSort(target, left, right, count, K):
    if left < right:
        mid = (left + right) // 2
        
        count = mergeSort(target, left, mid, count, K)
        count = mergeSort(target, mid + 1, right, count, K)
        count = merge(target, left, mid, right, count, K)
    
    return count

# [def(list(int), int, int, int) -> int] merge
# A[left..mid]와 A[mid+1..right]를 병합하여 오름차순 정렬된 상태로 만드는 함수
def merge(target, left, mid, right, count, K):
    i = left
    j = mid + 1
    tmp = list()
    
    while i <= mid and j <= right:
        if target[i] <= target[j]:
            tmp.append(target[i])
            i += 1
        else:
            tmp.append(target[j])
            j += 1
    
    while i <= mid:
        tmp.append(target[i])
        i += 1
    while j <= right:
        tmp.append(target[j])
        j += 1
    
    i = left
    t = 0
    while i <= right:
        count += 1
        if count == K:
            print(tmp[t])
        target[i] = tmp[t]
        i += 1
        t += 1
    
    return count

# [int, int] N, K
# N: 리스트 A의 크기 (범위(자연수): 5 <= N <= 500,000)
# K: 저장 횟수 (범위(자연수): 1 <= K <= 10^8)
N, K = map(int, input().split())

# [list(int)] A: 입력 받은 수를 저장한 리스트 (길이: N)
A = list(map(int, input().split()))

# mergeSort 실행
count = mergeSort(A, 0, N - 1, 0, K)

# K번째 값이 출력되지 않았다면 -1 출력
if count < K:
    print(-1)