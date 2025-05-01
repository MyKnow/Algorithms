import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

LIS = []

for a in A:
    idx = bisect_left(LIS, a)
    
    if idx == len(LIS):
        LIS.append(a)
    else:
        LIS[idx] = a

print(len(LIS))