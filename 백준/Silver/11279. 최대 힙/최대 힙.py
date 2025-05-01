import sys, heapq

read = sys.stdin.read
write = sys.stdout.write
data = read().split()

X = map(int, data[1:])

push = heapq.heappush
pop = heapq.heappop

pq = []
result = []

for x in X:
    if x != 0:
        # Make x negative to make max-heap
        push(pq, -x)
    else:
        result.append(-pop(pq) if pq else 0)

write("\n".join(map(str, result)) + "\n")