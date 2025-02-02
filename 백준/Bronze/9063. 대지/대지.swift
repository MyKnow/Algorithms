// [Int] N (immutable): 좌표의 개수 (범위: 1 <= N <= 100,000)
let N: Int = Int(readLine() ?? "1") ?? 1
    
// [Int] min_x, min_y, max_x, max_y (mutable): 좌하단과 우상단 좌표를 저장하는 변수
// 각 변수의 초기값은 의도에 맞게 입력 범위의 최대값, 최소값으로 초기화한다.
var (min_x, min_y): (Int, Int) = (10000, 10000)
var (max_x, max_y): (Int, Int) = (-10000, -10000)

for _ in 0..<N {
    // [Int] x, y: 입력 받은 좌표 (범위(정수): -10,000 <= x, y <= 10,000)
    let arrayOfInput: Array<Int> = (readLine() ?? "0 0").split(separator: " ").map { Int($0) ?? 0}
    let (x, y): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])
    
    // 각 좌표를 조건에 맞게 변경해나간다.
    min_x = [min_x, x].min() ?? 0
    min_y = [min_y, y].min() ?? 0
    max_x = [max_x, x].max() ?? 0
    max_y = [max_y, y].max() ?? 0
}
    
// 좌하단, 우상단 좌표를 통해 넓이 계산 및 출력
print((max_x - min_x) * (max_y - min_y))