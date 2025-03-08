import Foundation

// [func(Int, Int, Int, Int)] hanoi: 하노이 과정을 출력하는 함수
// [Int] n: 첫 번째 장대에 쌓인 원판 개수
// [Int] start: 옮길 장대의 번호
// [Int] end: 목표 장대의 번호
// [Int] sub: 보조 장대의 번호
func hanoi(_ n: Int, _ start: Int, _ end: Int, _ sub: Int) {
    if (n == 1) {
        print("\(start) \(end)")
    }
    else {
        hanoi(n-1, start, sub, end)
        print("\(start) \(end)")
        hanoi(n-1, sub, end, start)
    }
}

// [Int] N (immutable): 첫 번째 장대에 쌓인 원판 개수 (범위: 1 <= N <= 20)  
if let input = readLine(), let N = Int(input) {
    // 원판을 옮기는 횟수는 2^N-1이다.
    print(Int(pow(2, Double(N))) - 1)

    // 원판을 옮기고 과정을 출력한다.
    hanoi(N, 1, 3, 2)
}