// N: Int (immutable)
// description: An integer that represents length of Ai
// range: 1 ≤ N ≤ 1,000
if let input: String = readLine(), let N: Int = Int(input) {
    // Ai: [Int] (immutable)
    // description: An array of integers that stores sequences for finding bitonic sequences
    // length: N
    // range: 1 ≤ Ai ≤ 1,000
    let Ai: [Int] = (readLine() ?? "1").split(separator: " ").compactMap { Int($0) }
    
    // dp: [Int] (mutable)
    // description: An array of integers to store lengths of LIS for each index
    // length: N
    var dp = [Int](repeating: 1, count: N)
    
    // reverseDP: [Int] (mutable)
    // description: An array of integers to store lengths of LDS for each index
    // length: N
    var reverseDP = [Int](repeating: 1, count: N)
    
    // Update dp
    for i in 0..<N {
        for j in 0..<i {
            if Ai[i] > Ai[j] {
                dp[i] = max(dp[i], dp[j] + 1)
            }
        }
    }
    
    // Update reverseDP
    for i in stride(from: N-1, through: 0, by: -1) {
        for j in stride(from: N-1, to: i, by: -1) {
            if Ai[i] > Ai[j] {
                reverseDP[i] = max(reverseDP[i], reverseDP[j] + 1)
            }
        }
    }
    
    // Print by subtracting 1 from the maximum value from the sum of dp and reverseDP
    if let max = zip(dp, reverseDP).map({ $0 + $1 }).max() {
        print(max-1)
    }
}