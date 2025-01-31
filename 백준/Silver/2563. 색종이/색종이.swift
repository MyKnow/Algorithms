// [Array<Array<Bool>>] whitePaper (mutable): 가로, 세로의 길이가 각각 100인 정사각형 모양의 흰색 도화지
var whitePaper: [[Bool]] = [[Bool]](repeating: [Bool](repeating: false, count: 100), count: 100)

// [Int] N (immutable): 검은색 색종이 개수 (N <= 100)
let N: Int = Int(readLine() ?? "0") ?? 0

// N개의 검은색 색종이(가로, 세로 길이가 10인 정사각형)를 흰색 도화지에 붙인다.
for _ in 0..<N {
    // [Tuple(Int, Int)] xPoint, yPoint (imutable): 검은색 색종이의 좌상단 꼭지점의 x, y 좌표 
    // 예시에서는 좌하단 좌표를 가리키지만, 변환을 생략하기 위해 x축에 대해 뒤집은 모양으로 그림.
    let arrayOfPoint: Array<Int> = (readLine() ?? "1 1").split(separator: " ").map { Int($0) ?? 1}
    let (xPoint, yPoint): (Int, Int) = (arrayOfPoint[0], arrayOfPoint[1])
    
    // xPoint, yPoint부터 각각 +10까지 True로 바꿔서 검은색 색종이 영역임을 가리킨다.
    for x in xPoint..<xPoint+10 {
        for y in yPoint..<yPoint+10 {
            whitePaper[x][y] = true
        }
    }
}

// whitePaper 변수에서 True의 개수를 세어 넓이를 구한다.
var sumOfBlack: Int = 0
for x in 0..<100 {
    for y in 0..<100 {
        if (whitePaper[x][y]) {
            sumOfBlack+=1
        }
    }
}
            
print(sumOfBlack)