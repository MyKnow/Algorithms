// sqrt 함수를 사용하기 위해서 Foundation Import
import Foundation

// [Int] N (mutable): 소인수분해를 진행 할 정수 (범위: 1 <= N <= 10,000,000)
var N: Int = Int(readLine() ?? "1") ?? 1

// N이 1인 경우 아무것도 출력하지 않는다.
if (N != 1) {
    // [Array<Int>] resultOfPrimeFactorization (mutable): 소인수분해를 진행한 결과를 저장하는 배열
    var resultOfPrimeFactorization: Array<Int> = [Int]()

    // 제곱근까지만 소인수분해를 진행하게 해서 시간복잡도를 개선한다.
    // 제곱근 연산값이 0이 되면 유효한 범위가 아니게 되므로, max를 통해서 방지한다.
    for number in 2...max(2, Int(sqrt(Double(N)))) {
        // number로 나눌 수 없을 때까지 반복한다.
        while(N % number == 0) {
            resultOfPrimeFactorization.append(number)
            N /= number
        }
    }
    
    // 만약 소인수분해를 진행하고 나머지가 있다면, 배열에 추가함.
    if (N > 1) {
        resultOfPrimeFactorization.append(N)
    }

    // resultOfPrimeFactorization의 요소들을 출력
    print(resultOfPrimeFactorization.map { String($0) }.joined(separator: "\n"))
}