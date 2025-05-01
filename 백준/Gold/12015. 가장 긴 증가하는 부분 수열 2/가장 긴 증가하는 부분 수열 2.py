def binarySearch(lst, target):
    start = 0
    end = len(lst)
    
    while start < end:
        mid = (start + end) // 2
        
        if lst[mid] < target:
            start = mid + 1
        else:
            end = mid
            
    return start

N = int(input())
A = list(map(int, input().split()))

LIS = []

for a in A:
    idx = binarySearch(LIS, a)
    
    if idx == len(LIS):
        LIS.append(a)
    else:
        LIS[idx] = a

print(len(LIS))