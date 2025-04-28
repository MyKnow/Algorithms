func solution(_ squares: inout [Int]) {
    squares.append(0)
    
    var maxArea: Int = 0
    
    var stack = [(Int, Int)]()
    for idx in 1..<squares.count {
        var currentIdx: Int = idx
        let currentHeight: Int = squares[idx]

        while let (topIdx, topHeight): (Int, Int) = stack.last {
            if topHeight >= currentHeight {
                currentIdx = topIdx
                stack.removeLast()

                maxArea = max(maxArea, (idx-currentIdx) * topHeight)
            } else {
                break
            }
        }
        
        stack.append( (currentIdx, currentHeight) )
    }

    print(maxArea)
}

while let input: String = readLine() {
    var squares: [Int] = input.split(separator: " ").compactMap { Int($0) }

    let n: Int = squares[0]
    if n == 0 {
        break
    }
    
    solution(&squares)
}