# [int] M: 1 이상, N 이하의 자연수
M = int(input())

# [int] N: M 이상, 10,000 이하의 자연수
N = int(input())

# [list(int)] listOfPrime: 찾은 소수를 저장하는 리스트
listOfPrime = []

# M에서 N 사이에 있는 소수를 찾는다.
for number in range(M, N+1):
    # 만약 주어진 수가 1 이하라면 소수가 아니므로 넘어간다.
    if (number < 2):
        continue
        
    # n으로 나누어 떨어지는 수가 없다면 number를 리스트에 추가한다.
    for n in range(2, number):
        if (number % n == 0):
            break
    else :
        listOfPrime.append(number)
        
# 만약 소수가 없다면 -1만 출력한다.
if (len(listOfPrime) == 0) :
    print(-1)
else :
    # listOfPrime의 합계 출력
    print(sum(listOfPrime))

    # listOfPrime의 최솟값 출력
    print(min(listOfPrime))