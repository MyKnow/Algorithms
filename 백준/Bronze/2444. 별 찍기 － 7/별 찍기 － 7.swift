// [Int] N (immutable): 마름모의 대각선 길이 / 2 + 1 (1 <= N <= 100)
let N: Int = Int(readLine() ?? "1") ?? 1

// 위쪽 부분 출력 (중앙 포함)
for i in 0..<N {
    // 공백 출력
    print(String(repeating: " ", count: (N - i - 1)), terminator: "")
    // 별 출력
    print(String(repeating: "*", count: (2 * i + 1)))
}

// 아래쪽 부분 출력
for j in 0..<(N - 1) {
    // 공백 출력
    print(String(repeating: " ", count: (j + 1)), terminator: "")
    // 별 출력
    print(String(repeating: "*", count: (2 * (N - j - 2) + 1)))
}