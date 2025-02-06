import sys

input = sys.stdin.readline

# [int] N, M
# N: 듣도 못한 사람의 수 
# M: 보도 못한 사람의 수
# (범위(자연수): <= 20)
N, M = map(int, input().split())

# [set(int)] setOfN: 듣도 못한 사람을 저장하는 집합 (길이: N)
setOfN = set()

# [set(int)] setOfM: 보도 못한 사람을 저장하는 집합 (길이: M)
setOfM = set()

for _ in range(N):
    setOfN.add(input().strip())
    
for _ in range(M):
    setOfM.add(input().strip())
    
# [set(int)] setOfIntersection: 듣도 보도 못한 사람을 저장하는 집합 (길이: <= N, M)
setOfIntersection = setOfN.intersection(setOfM)

# 출력
print(len(setOfIntersection))
print("\n".join(sorted(list(setOfIntersection))))