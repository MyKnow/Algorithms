// [func<[Bool], [Bool], [Bool], int] solution
// 퀸을 조건에 맞게 배치하는 방법의 수(count)를 업데이트 하는 함수
// [inout Array<Bool>] bRow: 정사각형 맵을 선형화한 배열
// [inout Array<Bool>] bLT2RD: 선형화된 y = -x 대각선 리스트
// [inout Array<Bool>] bLD2RT: 선형화된 y = x 대각선 리스트
// [Int] row: 현재 탐색 중인 행 번호 및 퀸을 배치한 개수
func solution(
    _ bRow: inout [Bool],
    _ bLT2RD: inout [Bool],
    _ bLD2RT: inout [Bool],
    _ row: Int
) {
    // 전역 변수를 줄이기 위해 행의 길이 사용
    let N: Int = bRow.count
    
    // 1. 마지막 행까지 탐색했다면 모든 퀸을 배치한 것이므로 count를 증가시킨다.
    if (row == N) {
        count += 1
        return
    }
    // 2. 전체 열을 탐색한다.
    for col in 0..<N {
        // 2-1. 현재 행 내부에 퀸이 없거나
        // 2-2. 현재 [col][row] 좌표에서 y = -x 대각선에 퀸이 없거나
        // 2-3. 현재 [col][row] 좌표에서 y = x 대각선에 퀸이 없다면 배치할 수 있음.
        if (
            bRow[col] != true &&
            bLT2RD[(N-1)+col-row] != true &&
            bLD2RT[col + row] != true 
        ) {
            // 3. 현재 좌표에 퀸 배치
            bRow[col] = true
            bLT2RD[(N-1)+col-row] = true
            bLD2RT[col + row] = true 
            
            // 4. 이제 같은 행에 퀸을 배치할 수 없으므로, 다음 행으로 이동함.
            solution(&bRow, &bLT2RD, &bLD2RT, row+1)
            
            // 5. 모든 행을 탐색하고 왔으므로, 두번째 열에서 탐색하기 위해 백트래킹
            bRow[col] = false
            bLT2RD[(N-1)+col-row] = false
            bLD2RT[col + row] = false 
        }
    }
}

// [Int] count (mutable): 퀸을 배치하는 방법의 개수
var count: Int = 0

// [Int] N (immutable): 정사각형 체스판의 길이와 퀸의 개수 (범위(자연수): 1 ≤ N ≤ 15)
if let input: String = readLine(), let N: Int = Int(input) {
    // [Array<Bool>] bRow (mutable): 정사각형 맵을 선형화한 배열
    // 길이: N, 초기값: false (점유한 퀸 없음)
    var bRow: [Bool] = [Bool](repeating: false, count: N)

    // [Array<Bool>] bLT2RD (mutable): 선형화된 y = -x 대각선 리스트
    // 길이: 2*(N-1)+1, 초기값: false (점유한 퀸 없음)
    var bLT2RD: [Bool] = [Bool](repeating: false, count: 2*(N-1)+1)

    // [Array<Bool>] bLD2RT (mutable): 선형화된 y = x 대각선 리스트
    // 길이: 2*(N-1)+1, 초기값: false (점유한 퀸 없음)
    var bLD2RT: [Bool] = [Bool](repeating: false, count: 2*(N-1)+1)
    
    // 계산 수행
    solution(&bRow, &bLT2RD, &bLD2RT, 0)
    
    // count 출력
    print(count)
}