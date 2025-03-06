// [func(Int) -> Int] factorial: 정수 N을 입력받아서 N!을 반환하는 함수
func factorial(_ target: Int) -> Int {
    if (target <= 1) {
        return 1
    }
    return target * factorial(target-1)
}

// [Int] N (immutable): 팩토리얼을 찾을 정수 (범위: 0 ≤ N ≤ 20)
if let N = Int(readLine() ?? "") {
    print(factorial(N))
}