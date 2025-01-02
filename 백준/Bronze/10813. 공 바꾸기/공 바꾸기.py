# N: int - 가지고 있는 바구니의 개수 (1 <= N<= 100)
# M: int - 공을 바꾸려는 횟수 (1 <= M <= 100)
N, M = map(int, input().split())
        
# bucket: list - 공이 들어있는 바구니 list (길이: N)
# 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있음
bucket = list(range(1, N+1, 1))
    
# 각 반복마다 i와 j번째 바구니에 들어있는 공을 서로 교환한다.
for _ in range(M):
    # i: int - 공을 교환할 바구니 중 첫번째 ( 1 <= i <= j <= N)
    # j: int - 공을 교환할 바구니 중 두번째 ( 1 <= i <= j <= N)
    i, j = map(int, input().split())
            
    # k: int - 공을 교환하기 위해서 사용하는 임시 바구니
    # 임시 바구니에 i-1번째 바구니의 공을 옮긴다
    k = bucket[i-1]
        
    # i-1번째 바구니에 j-1번째 바구니의 공을 넣는다.
    bucket[i-1] = bucket[j-1]
    
    # j-1번째 바구니에 임시 바구니의 공을 넣는다.
    bucket[j-1] = k
    
# 공을 모두 다 교환하면 각 바구니의 공을 출력한다.
for number in bucket :
    print(number, end=" ")