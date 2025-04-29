import sys

input = sys.stdin.readline

def binarySearch(target, lst):
    start = 0
    end = max(lst)

    while(start<=end):
        mid = (start+end) // 2

        total = sum(t - mid for t in trees if t > mid)

        if total >= target:
            start = mid + 1
        else:
            end = mid - 1

    return end

N, M = map(int, input().split())

trees = list(map(int, input().split()))

print(binarySearch(M, trees))