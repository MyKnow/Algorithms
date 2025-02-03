# [int] a1, a0: 함수 f(n)을 나타내는 정수 (범위(정수): 0 ≤ |a_i| ≤ 100)
a1, a0 = map(int, input().split())

# [int] c: 양의 정수 (범위(정수): 1 ≤ c ≤ 100)
c = int(input())

# [int] n0: 양의 정수 (범위(정수): 1 ≤ n0 ≤ 100)
n0 = int(input())

# f(n) = a1*n + a0
# f(n) <= c * g(n) (모든 n은 n0 이상)
# 위 두 조건을 만족할 경우 1, 아니면 0을 출력하면 된다.

# [int] fn: fn 함수값
fn = a1 * n0 + a0

# 이 때, a0이 음의 정수일 때 예외가 생길 수 있다.
# 따라서, a1이 c보다 작거나 같아야 한다는 예외 조건을 추가해야 한다.
if (fn <= c * n0 and a1 <= c) :
    print(1)
else :
    print(0)