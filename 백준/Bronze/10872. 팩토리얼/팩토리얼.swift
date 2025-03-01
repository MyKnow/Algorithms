// [Int] N (immutable): 팩토리얼을 찾을 정수 (범위: 0 ≤ N ≤ 12)
if let N: Int = Int(readLine() ?? "0") {
    // [Int] fact (mutable): 답을 계산하는 변수
    var fact: Int = 1
    
    // 1부터 N까지 fact에 곱함
    for n in 1...max(N, 1) {
        fact = fact * n
    }

    // 답 출력
    print(fact)
}