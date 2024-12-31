# [int] N : 바구니의 수 (1 <= N <= 100)
# [int] M : 공을 넣을 횟수 (1 <= M <= 100)
N, M = map(int, input().split())

# [list] bucket : 바구니 list
# N에 따라 바구니 초기값 변경
bucket = [0]*N

# i번 바구니부터 j번 바구니까지 k번 공을 넣는 것을 M번 수행한다.
for _ in range(M):
    # [int] i : 공을 넣을 바구니 (1<=i<=j<=N)
    # [int] j : 공을 넣을 바구니 (1<=i<=j<=N)
    # [int] k : 바구니들에 넣을 공 번호 (1<=k<=N)
    i, j, k = map(int, input().split())
    
    # i번 index부터 j번 index까지 k로 초기화한다.
    bucket[i-1:j] = [k] * (j - i + 1)
    
# 각 bucket들에서 공 번호를 확인한다.
for ball in bucket:
    print(ball, end=" ")
    