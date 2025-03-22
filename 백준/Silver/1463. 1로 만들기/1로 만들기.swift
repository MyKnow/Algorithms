// [Int] X (immutable): An integer that represents number to finding number of calculations
// : (range: 1 ≤ X ≤ 10^6)
if let input: String = readLine(), let X: Int = Int(input) {
    // Exception protection
    if (X < 3) {
        print(X-1)
    } else {
        // [ Array<Int> ] dp (mutable): Array of integers to store numbers of calculations in each index
        var dp = [Int](repeating: 0, count: X+1)
        // 1 dosn't require calculation.
        dp[1] = 0
        
        // Repeat from 2 to X
        for idx in 2...X {        
            // Each cases
            // 1. "idx" isn't divided into 2 or 3.
            dp[idx] = 1 + dp[idx-1]
            
            // 2. "idx" divided into 3
            if idx % 3 == 0 {
                dp[idx] = min(dp[idx], dp[idx/3] + 1)
            }
            // 3. "idx" divided into 2
            if idx % 2 == 0 {
                dp[idx] = min(dp[idx], dp[idx/2] + 1)
            }
        }
        print(dp[X])
    }
}