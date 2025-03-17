// [func(Int, Int, Int)] w
// : Function that returns result of calcuation by recursion with memoization
// 
// - Parameters
// [Int] a, b, c: Integer that points to each index in the array called dp
//
// - Return
// [Int]: Integer that value of dp[a][b][c]
func w(
    _ a: Int, 
    _ b: Int, 
    _ c: Int
) -> Int {
    if (a <= 0 || b <= 0 || c <= 0) {
        return 1
    }
    
    if (a > 20 || b > 20 || c > 20) {
        return w(20, 20, 20)
    }

    // Return self when dp has pre-calculate value at now index
    if (dp[a][b][c] != 0) {
        return dp[a][b][c]
    }

    if (a < b && b < c) {
        // Memoization
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    }
    else {
        // Memoization
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]
    }
}

// [ Array<Array<Array<Int>>> ] dp (mutable)
// : 3-Dimensional array of integer that store results of function w
var dp =  [[[Int]]](repeating: [[Int]](repeating: [Int](repeating: 0, count: 21), count: 21), count: 21)

while (true) {
    if let input = readLine() {
        // [Int] a, b, c (immutable)
        // : Integer that points to each index in the array called 
        let arrayOfInput: [Int] = input.split(separator: " ").compactMap { Int($0) }
        let a: Int = arrayOfInput[0]
        let b: Int = arrayOfInput[1]
        let c: Int = arrayOfInput[2]
        
        if (a == b && b == c && c == -1) {
            break
        }
        
        print("w(\(a), \(b), \(c)) = \(w(a, b, c))")
    }
}