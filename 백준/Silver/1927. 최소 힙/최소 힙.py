import sys, heapq

input = sys.stdin.read
write = sys.stdout.write

push = heapq.heappush
pop = heapq.heappop

data = input().split()
N = data[0]
X = map(int, data[1:])

# Min-Heap
pq = []
result = []
for x in X:
    if x != 0:
        # Push original "x" to "pq" to make min-heap
        push(pq, x)
    elif pq:
        result.append( pop(pq) )
    else:
        result.append( 0 )

print("\n".join(map(str, result)))