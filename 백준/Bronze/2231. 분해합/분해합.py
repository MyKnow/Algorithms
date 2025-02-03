# [int] N: 분해합 (범위(자연수): 1 <= N <= 1,000,000)
N = int(input())

# [list(int)] listOfN: N의 각 자릿수를 따로 저장한 리스트
listOfN = list(map(int, str(N)))

# 1. 분해합의 생성자 M은 분해합 N의 길이보다 1 작거나 같다.
# 2. 생성자 M의 범위: (1 <= M <= N)
# 3. 여기서, 단순히 1부터 시작하는 게 아니라, (분해합의 앞자리 - 1)*(10**분해합의 자릿수-1) - (분해합의 자릿수*9)에서 시작하면 의미없는 계산을 생략할 수 있다.
# [int] start: 생성자 BruteForce의 최소 범위
# start = max(1, (listOfN[0]-1) * (10**len(listOfN)-1) - (len(listOfN)*9))

for number in range(1, N):
    # [list(int)] listOfM: number의 각 자릿수를 따로 저장한 리스트
    listOfM = list(map(int, str(number)))
    
    if (number+sum(listOfM) == N):
        print(number)
        break
else :
    print(0)