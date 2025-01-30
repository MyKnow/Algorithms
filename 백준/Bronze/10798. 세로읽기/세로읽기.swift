// [Array<Array<String>>] matrix (mutable): 주어진 글자들을 저장하는 2차원 배열 (5행 고정)
var matrix: [[String]] = [[String]]()

// [Int] maxLength (mutable): matrix의 최대 행 길이
var maxLength: Int = 0

for _ in 0..<5 {
    // 입력된 문자열을 matrix에 저장
    let row: Array<String> = readLine()?.map { String($0) } ?? []
    matrix.append(row)
    maxLength = max(maxLength, row.count)
}

// 세로로 출력
for col in 0..<maxLength {
    for row in 0..<5 {
        // 만약 현재 인덱스가 존재한다면 출력
        if (matrix[row].count > col) {
            print(matrix[row][col], terminator: "")
        }
    }
}