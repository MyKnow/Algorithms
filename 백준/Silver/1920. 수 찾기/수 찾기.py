import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = map(int, input().split())

result = []
for b in B:
    result.append('1' if b in A else '0')

print('\n'.join(result))