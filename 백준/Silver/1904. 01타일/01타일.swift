// [func(Int) -> Int] solution
// function that returns the number of cases when placing n tiles
//
// - Parameters
// [Int] N: Integer that represents number of tiles
//
// - Returns
// [Int] dp[1]: Integer that represents number of cases
func solution(_ N: Int) -> Int {
    // [Array<Int>] dp (mutable): Array of integers that stores number of cases when placing n tiles
    var dp = [Int](repeating: 0, count: N+1)
    dp[N] = 1
    dp[N-1] = 2

    // Repeat from the back for memory savings
    for idx in stride(from: N-2, to: 0, by: -1) {
        // Update result with each previous values.
        dp[idx] = (dp[idx+1] + dp[idx+2]) % 15746
        // Pop the last index for memory savings
        dp.removeLast()
    }

    return dp[1]
}

// [Int] N (immutable): Integer that represents number of tiles
if let input = readLine(), let N = Int(input) {
    print(solution(N))
}