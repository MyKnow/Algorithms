N, K = map(int, input().split())

temps = list(map(int, input().split()))

pSum = list()

for idx, num in enumerate(temps):
    pSum.append( (0 if idx == 0 else pSum[-1]) + num)

maxValue = -100*1000_000
for idx in range(K-1, len(pSum)):
    maxValue = max(maxValue, pSum[idx] - (pSum[idx-K] if idx-K >= 0 else 0))

print(maxValue)