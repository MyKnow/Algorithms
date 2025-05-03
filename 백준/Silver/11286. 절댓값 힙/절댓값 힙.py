import sys
from heapq import heappop, heappush

# Read all input at once and split into tokens
input = sys.stdin.read
write = sys.stdout.write
data = input().split()

# Read the number of operations (not used in logic)
N = data[0]

X = map(int, data[1:])

# Min-heaps for positive and negative values
plusHeap = []
minusHeap = []

result = []

# Process each number
for x in X:
    if x > 0:
        heappush(plusHeap, x)
    elif x < 0:
        heappush(minusHeap, -x)
    else:
        tmp = 0
        if plusHeap and minusHeap:
            # Compare absolute values and pop the smaller one
            if plusHeap[0] < minusHeap[0]:
                tmp = heappop(plusHeap)
            else:
                tmp = -heappop(minusHeap)
        elif minusHeap:
            tmp = -heappop(minusHeap)
        elif plusHeap:
            tmp = heappop(plusHeap)
        result.append(tmp)

# Output the result
print("\n".join(map(str, result)))