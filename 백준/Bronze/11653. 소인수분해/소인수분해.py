# [int] N: 소인수분해를 진행 할 정수 (범위: 1 <= N <= 10,000,000)
N = int(input())

# N이 1인 경우 아무것도 출력하지 않는다.
if (N != 1):
    # [list(int)] resultOfPrimeFactorization: 소인수분해를 진행한 결과를 저장하는 리스트
    resultOfPrimeFactorization = []

    # 2부터 N의 제곱근까지만 나눠서 소인수를 찾으면 훨씬 빠르다.
    for number in range(2, int(N ** 0.5) + 1):
        # number로 나눌 수 없을 때까지 반복한다.
        while(N % number == 0):
            resultOfPrimeFactorization.append(number)
            N //= number
        
    # 소인수 분해를 진행하고 남은 N도 리스트에 추가한다.
    if (N > 1):
        resultOfPrimeFactorization.append(N)
            
    # resultOfPrimeFactorization의 요소들을 출력
    print("\n".join(map(str, resultOfPrimeFactorization)))