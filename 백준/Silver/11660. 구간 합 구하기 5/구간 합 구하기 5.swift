if let input: String = readLine() {
    let arrayOfInput: [Int] = input.split(separator: " ").compactMap { Int($0) }
    let N: Int = arrayOfInput[0]
    let M: Int = arrayOfInput[1]

    var pSum = [[Int]](
        repeating: [Int](
            repeating: 0,
            count: N+1
        ),
        count: N+1
    )

    for y in 1...N {
        if let line: String = readLine() {
            let lines: [Int] = line.split(separator: " ").compactMap { Int($0) }

            for x in 1...N {
                pSum[y][x] = lines[x-1] + pSum[y-1][x] + pSum[y][x-1] - pSum[y-1][x-1]
            }
        }
    }

    var results = [Int]()
    for _ in 0..<M {
        let p: [Int] = readLine()!.split(separator: " ").compactMap { Int($0) }
        let (y1, x1, y2, x2): (Int, Int, Int, Int) = (p[0], p[1], p[2], p[3])
        results.append ( pSum[y2][x2] - pSum[y2][x1-1] - pSum[y1-1][x2] + pSum[y1-1][x1-1] )
    }
    
    print(results.map { String($0) }.joined(separator: "\n") )
}