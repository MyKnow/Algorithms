# [int] N: 주어진 수의 개수 (범위: <= N)
N = int(input())

# [int] countOfPrime: 소수의 개수를 세는 변수
countOfPrime = 0

# [list(int)] numberList: 검사할 숫자들을 담는 리스트 (범위: <= 1,000, 길이: N)
numberList = list(map(int, input().split()))

for number in numberList:
    # 2 이하는 소수가 아님.
    if (number < 2):
        continue

    # 1과 자신을 제외한 수로 나눠지면 소수가 아님
    for n in range(2, number):
        if (number % n == 0):
            break

    # 끝까지 통과하면 countOfPrime에 1을 더한다.
    else:
        countOfPrime += 1
            
# 소수의 개수를 출력한다.
print(countOfPrime)