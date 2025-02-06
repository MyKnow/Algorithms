import sys

# [int] N, M
# N: 도감에 수록되어 있는 포켓몬의 개수
# M: 다솜이가 맞춰야 하는 문제의 개수
# 범위(자연수): 1 <= N, M <= 100,000
N, M = map(int, sys.stdin.readline().split())

# [dict(int, string)] dictOfPocketmon: 입력 받은 포켓몬의 (이름:번호)쌍을 저장하는 사전 (길이: N)
dictOfPocketmon = dict()

# 포켓몬의 개수만큼 사전을 초기화한다.
for index in range(1, N+1):
    name = sys.stdin.readline().strip()
    
    dictOfPocketmon[name] = index
    dictOfPocketmon[index] = name

# 문제의 수만큼 반복한다.
for _ in range(M):
    question = input()
    
    # 문제가 숫자라면 숫자를 키값으로 활용하여 이름을 출력한다.
    if (question.isdigit()):
        print(dictOfPocketmon[int(question)])
    # 문제가 이름이라면 이름을 키값으로 활용하여 번호를 출력한다.
    else :
        print(dictOfPocketmon[question])