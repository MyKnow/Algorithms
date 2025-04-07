if let inputOfSizes: String = readLine() {
    let arrayOfSizes: [Int] = inputOfSizes.split(separator: " ").compactMap { Int($0) }

    // N, M: Int (immutable)
    // description: Integers representing lengths of table: vertical, horizontal
    // range: 1 ≤ N, M ≤ 2,000
    //
    // K: Int (immutable)
    // description: An integer representing length of the new chessboard that jimin will make
    // range: 1 ≤ K ≤ min(N, M)
    let (N, M, K): (Int, Int, Int) = (arrayOfSizes[0], arrayOfSizes[1], arrayOfSizes[2])
    
    // pSumOfB, pSumOfW: [[Int]] (mutable)
    // description: 2-Dimensional lists of integers to store prefix sums that representing 
    // total number of repainting times in an incorrectly colored compartment.
    // length: (M+1) * (N+1)
    var pSumOfB = [[Int]](
        repeating: [Int](
            repeating: 0,
            count: M+1
        ),
        count: N+1
    )
    var pSumOfW: [[Int]] = pSumOfB // Deep copy
    
    for y in 1...N {
        if let inputOfLine: String = readLine() {
            // line: If the color of the board compartment is Black
            // it is True, otherwise False
            let line: [Bool] = inputOfLine.map { $0 == "B" }
            
            // crtB: Correct color of "black first board" in each index y
            var crtB: Bool = (y % 2 == 1 ? true : false)
        
            for x in 1...M {
                // If the current color is incorrect, add the sum of 1 and
                // 2D prefixes and update the current pSum.
                pSumOfB[y][x] = (line[x-1] == crtB ? 0 : 1) + pSumOfB[y-1][x] + pSumOfB[y][x-1] - pSumOfB[y-1][x-1]
                pSumOfW[y][x] = (line[x-1] != crtB ? 0 : 1) + pSumOfW[y-1][x] + pSumOfW[y][x-1] - pSumOfW[y-1][x-1]
        
                // Change the color of each variable to the opposite color.
                crtB = !crtB
            }
        }
    }
    
    // minValue: Int (mutable)
    // description: An integer to store minimum value of each pSum
    // initial: N*M
    var minValue: Int = N*M
    
    for yK in K...N {
        for xK in K...M {
            // sumOfB, sumOfW: Prefix sum of each color on (xK, yK) points
            let sumOfB = pSumOfB[yK][xK] - pSumOfB[yK-K][xK] - pSumOfB[yK][xK-K] + pSumOfB[yK-K][xK-K]
            let sumOfW = pSumOfW[yK][xK] - pSumOfW[yK-K][xK] - pSumOfW[yK][xK-K] + pSumOfW[yK-K][xK-K]
    
            // Update minValue to smallest value
            minValue = min(minValue, sumOfB, sumOfW)
        }
    }
    
    // Print answer
    print(minValue)
}