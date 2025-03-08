// [func(inout Array<Array<Character>, Int, Int, Int)] makeStar
// 3^k 길이의 정사각형 패턴에 공백을 뚫는 함수
// [inout Array<Array<Character>] k: 변경할 이중 배열
// [Int] level: 현재 재귀 레벨
// [Int] startX:  작업을 진행할 범위 중 좌상단의 X 좌표
// [Int] startY:  작업을 진행할 범위 중 좌상단의 Y 좌표
func makeStar(_ k: inout [[Character]], _ level: Int, _ startX: Int, _ startY: Int) {
    // 1. level이 1인 경우 더 이상 공백을 뚫을 수 없으므로 종료함.
    if (level == 1) {
        return
    }

    // [Int] subLen (immutable): 현재 정사각형의 한 변을 3분할한 길이
    let subLen: Int = level / 3
    
    // 2. 현재 정사각형에서 start와 end 좌표를 참고하여 구멍을 뚫는다.
    for x in startX+subLen..<startX+subLen*2 {
        for y in startY+subLen..<startY+subLen*2 {
            k[y][x] = " "
        }
    }
            
    // 3. 구멍을 뚫은 정사각형의 나머지 8개 부분에 대하여 재귀적으로 구멍을 뚫는다.
    for x in 0..<3 {
        for y in 0..<3 {
            // 중간 부분은 건너뛰기
            if (x != 1 || y != 1) { 
                makeStar(&k, subLen, startX + subLen * x, startY + subLen * y)
            }
        }
    }
}   

// [Int] N (immutable): 정사각형 모양의 재귀적인 별 패턴을 생성할 크기 (범위: 3^K -> 1 <= K < 8)
if let input = readLine(), let N = Int(input) {
    // [Array<Array<Character>>] square (mutable): 공백을 뚫을 사각형을 표현하는 이중 배열 (길이: N*N)
    var square = [[Character]](repeating: [Character](repeating: "*", count: N), count: N)

    // square에 규칙대로 구멍을 뚫는다.
    makeStar(&square, N, 0, 0)
    
    // square를 출력한다.
    for row in square {
        print(String(row))
    }
}