// [func(Int, Int) -> int] getGCD: 최대 공약수를 구하는 함수
func getGCD(_ a: Int, _ b: Int) -> Int {
    if (b == 0) {
        return a
    } else {
        return getGCD(b, a % b)
    }
}

// [func(Int, Int) -> int] getLCM: 최소 공배수를 구하는 함수
func getLCM(_ a: Int, _ b: Int) -> Int {
    return (a * b) / getGCD(a, b)
}

// [Int] T (immutable): 테스트 케이스의 개수 (범위(자연수): 1 ≤ T ≤ 1,000)
let T: Int = Int(readLine() ?? "1") ?? 1

// 테스트 케이스의 개수만큼 수행
for _ in 0..<T {
    // [Int] A, B (immutable): 최소 공배수를 구하고자 하는 두 자연수 (범위(자연수): 1 ≤ A, B ≤ 45,000)
    let arrayOfInput: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
    let (A, B): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])
    
    print(getLCM(A, B))
}