// [func(Int, Int) -> Int] comb: 입력된 두 자연수의 이항계수를 계산하여 반환하는 함수
func comb(_ n: Int, _ r: Int) -> Int {
    var result = 1
    
    for i in 0..<r {
        result = result * (n - i) / (i + 1)
    }
    
    return result
}

// [Int] T (immutable): 테스트 케이스의 개수
if let T: Int = Int(readLine() ?? "1") {
    for _ in 0..<T {
        // [Int] N, M (immutable): 강의 서쪽 사이트와 동쪽 사이트의 개수 (범위(정수): 0 < N ≤ M < 30)
        let arrayOfInput: [Int] = (readLine() ?? "0 0").split(separator: " ").compactMap { Int($0) }
        let (N, M): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

        print(comb(M, N))
    }
}