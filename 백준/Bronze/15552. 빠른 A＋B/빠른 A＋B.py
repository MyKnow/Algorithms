import sys

# T : 테스트케이스의 개수 1 <= T <= 1,000,000
T = int(sys.stdin.readline())

for _ in range(T): 
    A, B = map(int, sys.stdin.readline().split())
    
    # print 대신 sys.stdout.write를 사용하여 성능 최적화
    sys.stdout.write(f"{A + B}\n")