// [func(Int) -> Int] intSqrt: 이진 탐색 기반 제곱근 반환 함수
func intSqrt(_ number: Int) -> Int {
    if number < 2 { return number }  // 0과 1의 제곱근은 자기 자신

    var left = 1, right = number
    var result = 1

    while left <= right {
        let mid = left + (right - left) / 2
        if mid * mid <= number {
            result = mid
            left = mid + 1  // 더 큰 값 탐색
        } else {
            right = mid - 1  // 더 작은 값 탐색
        }
    }
    
    return result  // number 이하의 가장 큰 정수 제곱근
}

// [func(int) -> bool] isPrime: 주어진 자연수가 소수인지 판별하는 함수
func isPrime(_ number: Int) -> Bool {
    // 0, 1은 소수가 아님
    if (number < 2) {
        return false
    }
    // 2, 3은 소수임
    else if (number < 4) {
        return true
    }
    
    // [Int] squareRoot (immutable): number의 제곱근
    let squareRoot: Int = intSqrt(number)
    
    // 2부터 number의 제곱근까지 i를 증가시켜서, number가 i로 나누어 떨어지는 지 확인함.
    for i in 2...squareRoot {
        if (number % i == 0) {
            return false
        }
    }
    
    return true
}
    

// [Int] N (immutable): 테스트 케이스의 개수
let N: Int = Int(readLine() ?? "1") ?? 1

for _ in 0..<N {
    // [Int] n (mutable): 본인보다 크거나 같은 소수를 찾을 기준이 되는 정수 (범위(정수): 0 <= n <= 4*10^9)
    var n : Int = Int(readLine() ?? "0") ?? 0
    
    while(!isPrime(n)) {
        n+=1
    }
    
    // n을 출력한다.
    print(n)
}