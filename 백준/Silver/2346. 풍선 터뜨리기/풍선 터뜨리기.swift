// [Int] N (immutable): 풍선의 개수 (범위(자연수): 1 ≤ N ≤ 1,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Array<Int, Int>] balloons (mutable): 풍선의 순번과 값의 쌍이 저장된 배열
let numbers: Array<Int> = (readLine() ?? "1 2").split(separator: " ").compactMap { Int($0) }
var balloons: [(Int, Int)] = numbers.enumerated().map { ($0.offset + 1, $0.element) }

// Array<Int> result (mutable): 터뜨린 풍선의 순번을 저장하는 배열
var result: Array<Int> = [Int]()

// 풍선이 모두 터질 때까지 반복
while (balloons.count != 0) {
    // [(Int, Int)] offset, element (immutable): 풍선의 번호와 값 쌍
    let (offset, element): (Int, Int) = balloons.removeFirst()
    
    // offset을 result에 저장한다.
    result.append(offset)
    
    // [Int] bCount (immutable): balloons 배열의 길이
    let bCount: Int = balloons.count
    
    // balloons 배열의 길이가 2 이상일 때, 배열을 element 값에 따라 회전 시킨다.
    if (bCount >= 2) {
        // [Int] shift (mutable): 배열 길이를 초과하는 이동을 방지하는 변수
        var shift: Int = abs(element) % bCount
        
        // element 값이 양수라면 왼쪽으로, 음수라면 오른쪽으로 회전 시킨다.
        if (element > 0) {
            // removeFirst에 의해 풍선이 하나 사라졌으므로 shift도 -1 한다.
            shift = (shift - 1 + bCount) % bCount

            // 왼쪽으로 배열을 회전 시키고 저장한다.
            let left = balloons[0..<shift]
            let right = balloons[shift..<bCount]
            balloons = Array(right+left)
        } else {
            let shiftAbs = bCount - shift
            let left = balloons[0..<shiftAbs]
            let right = balloons[shiftAbs..<bCount]
            balloons = Array(right + left)
        }
    }
}

print(result.map { String($0) }.joined(separator: " "))