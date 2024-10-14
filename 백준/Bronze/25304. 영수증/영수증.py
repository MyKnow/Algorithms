# X : 영수증에 적힌 총 금액
X = int(input())

# N : 영수증에 적힌 구매한 물건의 종류와 수
N = int(input())

result = 0
for i in range(N):
    price, count = map(int, input().split())
    result += (price * count)

if X == result :
    print("Yes")
else :
    print("No")