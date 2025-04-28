import sys

input = sys.stdin.readline

def binarySearch(n, lst):
    start = 1
    end = lst[-1]
    best = 0

    while(start<=end):
        mid = (start+end) // 2

        numberOfCable = 0
        for l in lst:
            numberOfCable += (l // mid)
            
        if numberOfCable >= n:
            best = mid
            start = mid + 1
        else:
            end = mid - 1
            
    return best

K, N = map(int, input().split())

lengths = []
for _ in range(K):
    lengths.append( int(input()) )
lengths.sort()

print(binarySearch(N, lengths))