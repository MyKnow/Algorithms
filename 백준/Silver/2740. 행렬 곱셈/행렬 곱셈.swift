func solution() {
    guard let inputOfNM: String = readLine() else {
        return
    }
    let arrayOfNM: [Int] = inputOfNM.split(separator: " ").compactMap { Int($0) }
    // N, M: int (immutable)
    // description: An integer representing length of matrix "A"
    // range: 1 ≤ N, M ≤ 100
    let (N, M): (Int, Int) = (arrayOfNM[0], arrayOfNM[1])
    
    // A: [[Int]] (mutable)
    // description: 2-Dimensional array of integers that represents matrix "A"
    // range: -100 ≤ A ≤ 100
    var A = [[Int]]()
    for _ in 0..<N {
        if let line: String = readLine() {
            A.append( line.split(separator: " ").compactMap { Int($0) } )
        }
    }
    
    guard let inputOfMK: String = readLine() else {
        return
    }
    let arrayOfMK: [Int] = inputOfMK.split(separator: " ").compactMap { Int($0) }
    // M, K: int (M isn't used, immutable)
    // description: An integer representing length of matrix "B"
    // range: 1 ≤ N, M ≤ 100
    let (_, K): (Int, Int) = (arrayOfMK[0], arrayOfMK[1])

    // B: [[Int]] (mutable)
    // description: 2-Dimensional array of integers that represents matrix "B"
    // range: -100 ≤ A ≤ 100
    var B = [[Int]]()
    for _ in 0..<M {
        if let line: String = readLine() {
            B.append( line.split(separator: " ").compactMap { Int($0) } )
        }
    }
    
    for row in A {
        // tmp: [Int] (mutable)
        // description: An array of integers to store result of matrix multiplication in each row
        // length: K
        // initial: 0
        var tmp = [Int](
            repeating: 0,
            count: K
        )
    
        // Double repeat statement for matrix "B"
        for y in 0..<K {
            for x in 0..<M {
                // Add row[y] times each column of B to tmp[y]
                tmp[y] += row[x] * B[x][y]
            }
        }
    
        // Print tmp
        print(tmp.map { String($0) }.joined(separator: " "))
    }
}

// Call function
solution()