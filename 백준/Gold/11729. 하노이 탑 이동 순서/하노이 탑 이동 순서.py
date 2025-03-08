# [def(int, int, int, int)] hanoi: 하노이 과정을 출력하는 함수
# [int] n: 첫 번째 장대에 쌓인 원판 개수
# [int] start: 옮길 장대의 번호
# [int] end: 목표 장대의 번호
# [int] sub: 보조 장대의 번호
def hanoi(n, start, end, sub):
    if (n == 1):
        print(start, end)
    else:
        hanoi(n-1, start, sub, end)
        print(start, end)
        hanoi(n-1, sub, end, start)

# [int] N: 첫 번째 장대에 쌓인 원판 개수 (범위: 1 <= N <= 20)  
N = int(input())

# 원판을 옮기는 횟수는 2^N-1이다.
print(2**N-1)

# 원판을 옮기고 과정을 출력한다.
hanoi(N, 1, 3, 2)