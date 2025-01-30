// [Tuple(Int, Int, Int)] tupleOfMax (mutable): max값의 행, 열, 값을 저장하는 tuple
var tupleOfMax: (Int, Int, Int) = (-1, -1, -1)

for row in 0..<9 {
    //[Array<Int>] rowOfMatrix (immutable): 매트릭스의 현재 row
    let rowOfMatrix: Array<Int> = (readLine() ?? "1 2 3 4 5 6 7 8 9").split(separator: " ").map { Int($0) ?? 1}
    
    // rowOfMatrix를 순회하며 값 탐색
    for col in 0..<9 {
        // tupleOfMax에 저장된 값보다 크면 현재 row, col, rowOfMatrix[col]을 저장
        if (rowOfMatrix[col] > tupleOfMax.2) {
            tupleOfMax = (row, col, rowOfMatrix[col])   
        }
    }
}

// 값 출력
print(tupleOfMax.2)
print(String(tupleOfMax.0+1), terminator: " ")
print(String(tupleOfMax.1+1))