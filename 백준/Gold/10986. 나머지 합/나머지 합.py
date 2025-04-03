import sys

input = sys.stdin.read
print = sys.stdout.write

data = input().split()

N = int(data[0])
M = int(data[1])
A = list(map(int, data[2:]))

remainders = [0 for _ in range(M)]

pSum = 0

count = 0

for i in range(N):
    pSum += A[i]

    remainder = pSum % M

    if remainder == 0:
        count += 1
        
    remainders[remainder] += 1

for r in remainders:
    tmp = 0
    for i in range(1, r):
        tmp += i

    count += tmp

print(str(count)+"\n")