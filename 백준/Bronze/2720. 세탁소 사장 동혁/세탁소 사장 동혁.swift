// [Int] T (immutable): 테스트 케이스의 개수
let T: Int = Int(readLine() ?? "1") ?? 1

// T번 반복
for _ in 0..<T {
    // [Int] C (mutable): 거스름돈 (단위: 센트, 범위: 1 <= C <= 500)
    var C: Int = Int(readLine() ?? "1") ?? 1
    
    // [Int] Q (immutable): 쿼터의 개수 ($0.25 = 25센트)
    let Q: Int = C / 25
    C %= 25
    
    // [Int] D (immutable): 다임의 개수 ($0.10 = 10센트)
    let D: Int = C / 10
    C %= 10
    
    // [Int] N (immutable): 니켈의 개수 ($0.05 = 5센트)
    let N: Int = C / 5
    C %= 5
    
    // [Int] P (immutable): 페니의 개수 ($0.01 = 1센트)
    let P: Int = C / 1
    
    // 각 거스름돈을 공백으로 구분하여 출력
    print(Q, D, N, P)
}