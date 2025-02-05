// [Int] N (immutable): 입력 받을 점의 개수 (범위(정수): 1 <= N <= 100,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Array<Tuple<Int, Int>>] arrayOfPoints (mutable): 입력 받은 좌표를 저장하는 배열 (길이: N)
var arrayOfPoints: Array<(Int, Int)> = Array<(Int, Int)>()

for _ in 0..<N {
    let arrayOfInput: Array<Int> = (readLine() ?? "0 0").split(separator: " ").compactMap { Int($0) }
    arrayOfPoints.append( (arrayOfInput[0], arrayOfInput[1]) )
}
    
// tuple의 좌표를 기준으로 오름차순 정렬
arrayOfPoints.sort(by: { $0.0 == $1.0 ? $0.1 < $1.1 : $0.0 < $1.0 })

for (x, y) in arrayOfPoints {
    print("\(x) \(y)")
}