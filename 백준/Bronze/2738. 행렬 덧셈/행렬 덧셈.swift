//[Array<Int>] N, M (immutable): 행렬의 세로, 가로 길이 (N, M < 100)
let lengthOfMatrix: Array<Int> = (readLine() ?? "1 1").split(separator: " ").map { Int($0) ?? 1}
let (N, M): (Int, Int) = (lengthOfMatrix[0], lengthOfMatrix[1])

// [Array<Array<Int>>)] A (mutable): 원소의 절대값이 100 이하인 정수 행렬 A
var A: Array<Array<Int>> = [[Int]]()

// [Array<Array<Int>>)] B (mutable): 원소의 절대값이 100 이하인 정수 행렬 B
var B: Array<Array<Int>> = [[Int]]()

// A 행렬 초기화
for _ in 0..<N {
    A.append( (readLine() ?? "1").split(separator: " ").map {Int($0) ?? 1} )
}  
// B 행렬 초기화
for _ in 0..<N {
    B.append( (readLine() ?? "1").split(separator: " ").map {Int($0) ?? 1} )
}
// A, B 행렬 더한 결과 출력
for index in 0..<N {
    // [Array<Int>] sumRow (immutable): 각 매트릭스 row의 합(A[index] + B[index])의 결과물
    let sumRow: Array<Int> = zip(A[index], B[index]).map { $0+$1 }
    print(sumRow.map { String($0) }.joined(separator: " "))
}
