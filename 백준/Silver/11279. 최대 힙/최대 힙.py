import sys, heapq

input = sys.stdin.read
write = sys.stdout.write

data = input().split()

N = data[0]
X = map(int, data[1:])

pq = []
result = []
for x in X:
    if x != 0:
        # Make x negative to make max-heap, 
        heapq.heappush(pq, -x)
    else:
        if pq:
            result.append( -heapq.heappop(pq) )
        else:
            result.append( 0 )

write("\n".join(map(str, result))+"\n")