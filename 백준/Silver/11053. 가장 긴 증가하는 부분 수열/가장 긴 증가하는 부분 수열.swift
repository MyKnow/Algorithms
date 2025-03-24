// Int N (immutable): An integer that represents length of Ai
if let input: String = readLine(), let N: Int = Int(input) {
    // [Int] Ai (immutable): Array of integers that stores integers to find LIS
    let Ai: [Int] = (readLine() ?? "1").split(separator: " ").compactMap { Int($0) }

    // [Int] dp (mutable): Array of integers to store LIS at each index
    var dp = [Int](repeating: 1, count: N)

    // Int gMax (mutable): An integer to update maximum length of LIS
    var gMax: Int = 1
    
    for i in 1..<N {
        for j in 0..<i {
            if Ai[j] < Ai[i] {
                // Update dp[i] to a larger value between 1 and dp[j]+1
                dp[i] = max(dp[i], dp[j]+1)
            }
        }
        // Update gMax
        gMax = max(gMax, dp[i])
    }
    
    print(gMax)
}