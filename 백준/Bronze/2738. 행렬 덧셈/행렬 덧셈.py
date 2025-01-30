#[tuple(int, int)] N, M : 행렬의 세로, 가로 길이 (N, M < 100)
N, M = map(int, input().split())

# [list(list(int))] A : 원소의 절대값이 100 이하인 정수 행렬 A
A = [[0] * M for _ in range(N)]

# [list(list(int))] B : 원소의 절대값이 100 이하인 정수 행렬 B
B = [[0] * M for _ in range(N)]

# A 행렬 초기화
for index in range(N) :
    A[index] = list(map(int, input().split()))    
# B 행렬 초기화
for index in range(N) :
    B[index] = list(map(int, input().split()))
    
# A, B 행렬 더한 결과 출력
for index in range(N) :
    print(" ".join(map(str, [a+b for a, b in zip(A[index], B[index])])))