import sys

input = sys.stdin.read
print = sys.stdout.write

data = input().split()

S = data[0]
q = int(data[1])
queries = data[2:]

pSum = [[0] * (len(S)) for _ in range(26)]

for i in range(len(S)):
    idx = ord(S[i]) - ord('a')

    pSum[idx][i] = pSum[idx][i-1] + 1
    for j in range(26):
        if j != idx:
            pSum[j][i] = pSum[j][i-1]

results = []
for c, l, r in zip(queries[0::3], queries[1::3], queries[2::3]):
    cIdx = ord(c) - ord('a')
    l = int(l)
    r = int(r)

    if l-1 < 0:
        results.append(str(pSum[cIdx][r]))
    else:
        results.append(str(pSum[cIdx][r] - pSum[cIdx][l-1]))

print("\n".join(results))