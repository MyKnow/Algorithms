import sys
	
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

Pi = sorted(list(map(int, input().split())))

sumOfPi = 0
totalTime = 0

for t in Pi:
    sumOfPi += t
    totalTime += sumOfPi

print(f"{totalTime}\n")