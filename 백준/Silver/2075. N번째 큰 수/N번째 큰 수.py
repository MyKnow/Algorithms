import sys
from heapq import heappop, heappush

input = sys.stdin.readline

# Represents the table size and the index of number to print
N = int(input())

# Min-heap
pq = []

for idx in range(N):
    for val in map(int, input().split()):
        # Keep the length N
        heappush(pq, val)
        if len(pq) > N:
            heappop(pq)

# Print the Nth largest number
print(pq[0])  # The root of the heap will be the Nth largest value