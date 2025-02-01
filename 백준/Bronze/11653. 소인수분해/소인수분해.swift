// [Int] N (mutable): 소인수분해를 진행 할 정수 (범위: 1 <= N <= 10,000,000)
var N: Int = Int(readLine() ?? "1") ?? 1

// N이 1인 경우 아무것도 출력하지 않는다.
if (N != 1) {
    // [Array<Int>] resultOfPrimeFactorization (mutable): 소인수분해를 진행한 결과를 저장하는 리스트
    var resultOfPrimeFactorization: Array<Int> = [Int]()

    for number in 2...N {
        // number로 나눌 수 없을 때까지 반복한다.
        while(N % number == 0) {
            resultOfPrimeFactorization.append(number)
            N /= number
        }
    }

    // resultOfPrimeFactorization의 요소들을 출력
    print(resultOfPrimeFactorization.map { String($0) }.joined(separator: "\n"))
}