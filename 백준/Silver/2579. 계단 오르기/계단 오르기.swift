// [Int] n (immutable): An Integer that represents number of stairs
if let input = readLine(), let n: Int = Int(input) {
    // [ Array<Int> ] stairs (mutable): Array of integers that stores values of each stairs
    var stairs: [Int] = [0]
    
    // Append values of each stairs
    for _ in 0...n {
        if let line: String = readLine(), let val: Int = Int(line) {
            stairs.append ( val )
        }
    }
    
    // [ Array<Int> ] dp (mutable)
    // : Array of integers that stores calculated values
    var dp: [Int] = [Int](repeating: 0, count: n+1)
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]

    // Error Protection when n == 1
    if (n != 1) {
        for idx in 2...n {
            // Update dp[idx] with sum of the current step values and larger value between "oneStep" and "twoStep"
            let twoStep: Int = dp[max(idx-3, 0)] + stairs[idx-1]
            let ownStep: Int = dp[idx-2]
            dp[idx] = max(ownStep, twoStep) + stairs[idx]
        }
    }
    
    // Print nth dp
    print(dp[n])
}