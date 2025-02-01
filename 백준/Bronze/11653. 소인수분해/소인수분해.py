# [int] N: 소인수분해를 진행 할 정수 (범위: 1 <= N <= 10,000,000)
N = int(input())

# N이 1인 경우 아무것도 출력하지 않는다.
if (N != 1):
    # [list(int)] resultOfPrimeFactorization: 소인수분해를 진행한 결과를 저장하는 리스트
    resultOfPrimeFactorization = []

    for number in range(2, N+1):
        # number로 나눌 수 없을 때까지 반복한다.
        while(N % number == 0):
            resultOfPrimeFactorization.append(number)
            N //= number

    # resultOfPrimeFactorization의 요소들을 출력
    print("\n".join(map(str, resultOfPrimeFactorization)))