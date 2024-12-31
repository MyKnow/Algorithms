# [int] X : 필터링 기준 (1 <= X <= 10,000)
_, X = map(int, input().split())

# [list] A : 숫자를 담을 배열
A = map(int, input().split())

# X보다 작은 수만 출력한다.
for number in A:
    if (number < X) :
        print(number, end=" ")