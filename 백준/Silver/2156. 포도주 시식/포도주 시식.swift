// Int n (immutable): number of glass (range: 1 ≤ n ≤ 10,000)
if let input: String = readLine(), let n: Int = Int(input) {

    // [Int] glass (mutable): Array of integers that store amount of wine at each glass (range: ≤ 1,000, length: n)
    var glass = [Int]()
    while let line: String = readLine(), let intLine: Int = Int(line) {
        glass.append( intLine )
    }
    
    // [Int] dp (mutable): Array of integers to store the total amount of wine drinked by each index
    var dp = [Int](repeating: 0, count: n)
    dp[0] = glass[0]
    
    // Protection of IndexError
    if n > 1 {
        dp[1] = glass[0] + glass[1]
    } 
    if n > 2 {
        for idx in 2..<n {
            // Cases:
            // 1. Not drinking current wine
            // 2. Drinking idx-2 wine and current wine
            // 3. Drinking before and current wine
            // Update dp[idx] to largest of the three cases.
            dp[idx] = max( dp[idx-1], dp[idx-2]+glass[idx], (idx == 2 ? 0 : dp[idx-3]) + glass[idx-1] + glass[idx] )
        }
    }

    if let max: Int = dp.max() {
        print(max)
    }
}