import sys
	
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

lengths = list(map(int, input().split()))

prices = list(map(int, input().split()))

price = prices[0]
total = 0
for idx in range(N-1):
    total += price * lengths[idx]
    price = min(price, prices[idx+1])

print(f"{total}\n")