if let firstInput: String = readLine(), let secondInput: String = readLine() {
    // s1, s2: Array<Character> (immutable)
    // description: Array of character saved to obtain LCS in comparison with each sequence
    // length: <= 1,000
    let s1: [Character] = Array(firstInput)
    let s2: [Character] = Array(secondInput)
    
    // dp: [[Int]] (mutable)
    // description: 2 Dimensional-list to store LCS by comparing each sequence
    var dp = [[Int]](
        repeating: [Int](repeating: 0, count: s2.count + 1),
        count: s1.count + 1
    )
    
    for y in 1...s1.count {
        for x in 1...s2.count {
            // When each alphabet from s1 and s2 is same
            if (s1[y-1] == s2[x-1]) {
                // Update the length of current LCS with the previous caculation value
                dp[y][x] = dp[y-1][x-1] + 1
            }
            // When each alphabet is different
            else {
                // Update the length of the current LCS with the largest values in each previous calculation x-1 and y-1
                dp[y][x] = max(dp[y-1][x], dp[y][x-1])  
            }
        }
    }
            
    
    // Print maximum value of dp (LCS)
    if let lastRow = dp.last, let lastElement = lastRow.last {
        print(lastElement)
    }
}
    
    