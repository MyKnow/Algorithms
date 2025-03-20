// [Int] n (immutable): An Integer that represents height of triangle
if let input: String = readLine(), let n: Int = Int(input) {
    // [ Array<Array<Int>> ] dp: 2-Dimensional array of integers that stores values in triangle
    var dp = [[Int]]()
    
    // Append values in triangle to dp
    while let line: String = readLine() {
        let values: [Int] = line.split(separator: " ").compactMap { Int($0) }
        dp.append( values )
    }
    
    for idx in 1..<n {
        for vIdx in 0...idx {
            var left: Int = 0
            var right: Int = 0
            
            // Update left when exist value in the top left
            if (vIdx != 0) {
                left = dp[idx-1][vIdx-1]
            }
            // Update right when exist value in the top right
            if (vIdx != idx) {
                right = dp[idx-1][vIdx]                
            }
    
            // Update the current value by adding the larger value of top left or top right and the value in current position
            if let max: Int = [left, right].max() {
                dp[idx][vIdx] += max
            }
        }
    }
    
    // Print maximum value in dp
    if let max: Int = dp[n-1].max() {
        print(max)
    }
}