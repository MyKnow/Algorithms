import sys

input = sys.stdin.readline

def binarySearch(target, lst):
    start = 0
    end = max(lst)
    best = 0

    while(start<=end):
        mid = (start+end) // 2

        sumOfCutted = 0
        for h in lst:
            sumOfCutted += ( (h - mid) if h > mid else 0 )

        if sumOfCutted >= target:
            best = mid
            start = mid + 1
        else:
            end = mid - 1

    return best

N, M = map(int, input().split())

trees = list(map(int, input().split()))

print(binarySearch(M, trees))