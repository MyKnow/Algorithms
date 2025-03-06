count = 0

# [def(list(int), int, int) -> list(int)] mergeSort: 주어진 배열을 오름차순 정렬하는 함수
def mergeSort(target, left, right):
    
    if (left < right):
        mid = (left+right) // 2
        
        mergeSort(target, left, mid)
        mergeSort(target, mid+1, right)
        merge(target, left, mid, right)
        
# [def(list(int), int, int, int) -> list(int)] merge
# A[left..mid]와 A[mid+1..right]를 병합하여 오름차순 정렬된 상태로 만드는 함수
# 이 때, 좌측과 우측은 이미 오름차순으로 정렬되어 있다.
def merge(target, left, mid, right):
    i = left
    j = mid + 1
    tmp = list()
    
    while (i <= mid and j <= right):
        if (A[i] <= A[j]):
            tmp.append(A[i])
            i+=1
        else:
            tmp.append(A[j])
            j+=1
        
    while (i <= mid):
        tmp.append(A[i])
        i+=1
    while (j <= right):
        tmp.append(A[j])
        j+=1
    
    i = left
    t = 0
    while(i <= right):
        global count, K
        count += 1
        
        if (K == count):
            print(tmp[t])
        A[i] = tmp[t]
        i+=1
        t+=1
        
# [int, int] N, K
# N: 리스트 A의 크기 (범위(자연수): 5 <= N <= 500,000)
# K: 저장 횟수 (범위(자연수): 1 <= K <= 10^8)
N, K = map(int, input().split())

# [list(int)] A: 입력 받은 수를 저장한 리스트 (길이: N)
A = list(map(int, input().split()))

mergeSort(A, 0, N-1)

if K > count:
    print(-1)