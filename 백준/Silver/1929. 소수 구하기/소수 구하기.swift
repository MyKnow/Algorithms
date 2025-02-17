import Foundation

// [func(Int)->Bool] isPrimeNumber: 주어진 정수가 소수인지 확인하는 함수
func isPrimeNumber(_ integer: Int) -> Bool {
    // 0, 1은 소수가 아니다.
    if (integer <= 1) {
        return false
    }
    // 2, 3은 소수이다.
    else if (integer <= 3) {
        return true
    }
    
    // [Int] sqrtInt (immutable): 제곱근이 취해진 integer
    let sqrtInt: Int = Int(Double(integer).squareRoot())
    
    // 2부터 자기자신 이전까지 나누어 떨어지지 않으면 소수이다.
    for number in 2...sqrtInt {
        // 나누어 떨어지는 경우가 있으므로 즉시 False 반환
        if (integer % number == 0) {
            return false
        }
    }
    
    return true
}

// [Int] M, N (immutable): 소수를 찾을 정수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 1,000,000)
let arrayOfInput: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
let (M, N): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

for n in M...N {
    if (isPrimeNumber(n)) {
        print(n)
    }
}