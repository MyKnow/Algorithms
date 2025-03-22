import Foundation

// [ Int ] N (immutable): An integer that represents number of digits
let N = Int(readLine()!)!

// [ Array<Array<Int64>> ] dp (mutable): 2-Dimensional list that stores number of cases at each digit
var dp = Array(repeating: Array(repeating: Int64(0), count: 10), count: N)

// [ Int64 ] MOD (immutable): A constant to prevent integer overflow
let MOD: Int64 = 1_000_000_000

// Initialize the first row (0 is not possible, 1~9 are possible)
dp[0] = [0] + Array(repeating: 1, count: 9).map { Int64($0) }

for idx in 1..<N {
    // 0 is only possible if the previous number is 1
    dp[idx][0] = dp[idx - 1][1] % MOD
    // 9 is only possible if the previous number is 8
    dp[idx][9] = dp[idx - 1][8] % MOD

    for number in 1..<9 {
        dp[idx][number] = (dp[idx - 1][number - 1] + dp[idx - 1][number + 1]) % MOD
    }
}

// [ Int64 ] result (immutable): Sum of all cases at the last digit, modulo 1_000_000_000
let result = dp[N - 1].reduce(0) { ($0 + $1) % MOD }
print(result)