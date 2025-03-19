// [func(Int) -> Int] P
// : A Function that returns length of nth triangle
//
// - Parameter
// [Int] N: An Integer that represents index of 
// triangle to find the length of sides
//
// - Return
// [Int] dp[N]: An Integer that represents length of side of nth triangle
func P(_ N: Int) -> Int {
    // Return dp[N] if nth triangle has been calculated
    if (maxN > N) {
        return dp[N]
    }

    // Repeat maxN+1 to N+1 to reduce duplicate calculations
    for idx in maxN+1...N {
        dp[idx] = dp[idx-5] + dp[idx-1]
    }

    // Update maxN
    if (maxN < N) {
        maxN = N
    }

    return dp[N]
}

// [Int] T (immutable): Number of test cases
let input: String = readLine() ?? "1"
let T: Int = Int(input) ?? 1

// [Array<Int>] dp (mutable): Array of integer that store lengths of side of nth triangles
var dp = [Int](repeating: 0, count: 101)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2

// [Int] maxN (mutable): Integer that stores last calculated index
var maxN: Int = 4

while let input: String = readLine(), let N: Int = Int(input) {
    print(P(N))
}