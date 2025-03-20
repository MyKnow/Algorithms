// [Int] n (immutable): An Integer that represents number of houses
if let input: String = readLine(), let n: Int = Int(input) {
    // [Array<Int>] dp (mutable)
    // : 2-Dimensional array of integers that stores RGB painting cost value of each houses
    var dp = [[Int]]()
    
    for _ in 0..<n {
        // Append RGB painting cost values to dp
        if let rgb: String = readLine() {
            dp.append( rgb.split(separator: " ").compactMap { Int($0) } )
        }
    }
    
    // Update DP
    for idx in 1..<n {
        dp[idx][0] = min(dp[idx-1][1], dp[idx-1][2]) + dp[idx][0]
        dp[idx][1] = min(dp[idx-1][0], dp[idx-1][2]) + dp[idx][1]
        dp[idx][2] = min(dp[idx-1][0], dp[idx-1][1]) + dp[idx][2]
    }
    
    // Print minimum at dp[n-1]
    if let min = dp[n-1].min() {
        print(min)
    }
}