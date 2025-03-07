import sys

# [def(int) -> str] cantor: N에 대한 칸토어 집합의 근사를 출력하는 함수
def cantor(target):
    if (target == 0):
        return "-"
    else:
        blank = " " * (3**(target-1))
        return cantor(target-1) + blank + cantor(target-1)

# [list(int)] listOfN: 칸토어 집합의 근사를 만들 길이들을 저장하는 리스트 (범위(정수): 0 <= N <= 12)
listOfN = map(int, sys.stdin.read().split())

for N in listOfN:
    print(cantor(N))