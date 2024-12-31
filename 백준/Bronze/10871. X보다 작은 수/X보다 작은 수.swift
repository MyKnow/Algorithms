// [Int] N : Array 크기 (1 <= X <= 10,000)
// [Int] X : 필터링 기준 (1 <= X <= 10,000)
let inputOfFirstLine: Array<Int> = (readLine() ?? "1 1").split(separator: " ").map{ Int($0) ?? 1}
var N: Int = inputOfFirstLine[0]
var X: Int = inputOfFirstLine[1]

// [Array<Int>] A : 정수를 저장 할 Int 배열
let A: Array<Int> = (readLine() ?? "1 1").split(separator: " ").map{Int($0) ?? 0}

// X에 따라 출력 여부 결정
for i in 0..<N {
    if (A[i] < X) {
        print(A[i], terminator: " ")
    }
}