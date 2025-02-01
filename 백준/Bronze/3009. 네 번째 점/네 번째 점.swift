// [Array<Int>] arrayOfX (mutable): 등장한 x 좌표를 저장하는 배열
var arrayOfX: Array<Int> = [Int]()
// [Array<Int>] arrayOfY (mutable): 등장한 y 좌표를 저장하는 배열
var arrayOfY: Array<Int> = [Int]()

// 직사각형의 세 꼭짓점 좌표를 입력 받는다.
for _ in 0..<3 {
    // [Int] x, y (immutable): 각 꼭짓점의 x, y 좌표 (범위(자연수): 1 <= x, y <= 1,000)
    let arrayOfInput: Array<Int> = (readLine() ?? "1 1").split(separator: " ").map { Int($0) ?? 1}
    let x: Int = arrayOfInput[0]
    let y: Int = arrayOfInput[1]
    
    // 각 좌표에서 가장 적게 등장한 값이 찾고자 하는 점의 좌표이다.
    // 이미 각 리스트에 해당 값이 들어있으면 삭제하고, 없으면 추가한다.
    if let indexOfX = arrayOfX.firstIndex(of: x) {
        arrayOfX.remove(at: indexOfX)
    }
    else {
        arrayOfX.append(x)
    }
    
    if let indexOfY = arrayOfY.firstIndex(of: y) {
        arrayOfY.remove(at: indexOfY)
    }
    else {
        arrayOfY.append(y)
    }

}

// 각 list의 첫번째 값을 출력한다.
print("\(arrayOfX[0]) \(arrayOfY[0])")