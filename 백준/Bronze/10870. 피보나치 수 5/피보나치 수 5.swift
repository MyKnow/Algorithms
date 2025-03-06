// [func(Int) -> Int] fibonacci: 피보나치 수열의 N번째 수를 반환하는 함수
func fibonacci(_ target: Int) -> Int {
    if (target < 2) {
        return target
    }
    return fibonacci(target-1) + fibonacci(target-2)
}

// [Int] N (immutable): 피보나치 수를 찾을 수의 순번 (범위: 0 <= N <= 20)
if let N = Int(readLine() ?? "0") {
    print(fibonacci(N))
}