// [Int] N, M (immutable): 보드의 세로, 가로 길이 (범위(자연수): 8 <= N, M <= 50))
let arrayOfInput: Array<Int> = (readLine() ?? "8 8").split(separator: " ").compactMap { Int($0) }
let (N, M): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

// [Array<Array<String>>] board (immutable): 입력받은 N, M 크기의 보드판을 입력 받기 위한 이중 배열 (길이: N*M)
var board: Array<Array<String>> = [[String]]()

for _ in 0..<N {
    if let line = readLine() {
        // 한 줄을 문자 배열로 변환
        let strList: Array<String> = Array(line.map { String($0)}) 
        
        // board에 추가
        board.append(strList)      
    } else {
        // 기본값으로 "W"를 추가 (readLine이 nil인 경우)
        board.append(["W"]) 
    }
}

// [Int] minOfFixCount (mutable): 보드판을 칠해야 하는 정사각형 최소 개수 (초기값: N*M (모든 칸이 오류))
var minOfFixCount: Int = N*M

// index를 넘어가지 않도록 처리함.
for n in 0...N-8 {
    for m in 0...M-8 {
        // [Int] sumOfFix_W, sumOfFix_B (mutable): 다시 칠해야 하는 정사각형 개수를 저장하는 변수
        var sumOfFix_W: Int = 0  // 'W'로 시작하는 체스판
        var sumOfFix_B: Int = 0  // 'B'로 시작하는 체스판
        
        for y in 0..<8 {
            for x in 0..<8 {
                let nowColor: String = board[y+n][x+m]
                
                // 짝수 위치
                if ((x + y) % 2 == 0) {  
                    if nowColor != "W" {
                        sumOfFix_W += 1
                    }
                    if nowColor != "B" {
                        sumOfFix_B += 1
                    }
                }
                // 홀수 위치
                else {  
                    if nowColor != "B" {
                        sumOfFix_W += 1
                    }
                    if nowColor != "W" {
                        sumOfFix_B += 1
                    }
                }
            }
        }
        
        // 리스트에 sumOfFix를 추가함.
        minOfFixCount = [minOfFixCount, sumOfFix_W, sumOfFix_B].min() ?? 0
    }
}
        
// 모든 보드판을 탐색하여 countOfFix에 고쳐야 할 보드칸 개수가 저장되면, 그 중 최소값을 출력한다.
print(minOfFixCount)