# N: int - 바구니의 개수 (1 <= N <= 100)
# M: int - 바구니를 역순으로 만드는 횟수 (1 <= M <= 100)
N, M = map(int, input().split())

# bucket: list - 바구니 리스트 (길이: N)
bucket = [x for x in range(1, N+1)]

# M번에 걸쳐서, 매회 i-1부터 j-1번째까지의 바구니의 순서를 역순으로 변경한다.
for _ in range(M):
    # i: int - 역순으로 만들 바구니 중 제일 왼쪽 (1 <= i <= j <= N)
    # j: int - 역순으로 만들 바구니 중 제일 오른쪽 (1 <= i <= j <= N)
    i, j = map(int, input().split())
    
    # i-1부터 j-1까지의 index를 뒤집은 다음, 저장한다.
    bucket[i-1: j] = bucket[i-1: j][::-1]
    
for number in bucket:
    print(number, end=' ')