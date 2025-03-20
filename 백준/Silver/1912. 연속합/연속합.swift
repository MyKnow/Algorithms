// [Int] n (immutable): Number of integers to enter (range: 1 ≤ n ≤ 100,000)
if let input = readLine(), let n: Int = Int(input) {
    if let inputOfArray = readLine() {
        // [Array<Int>] arrayOfSequence (immutable): Array of integers that store integers to find max continuos sum
        let arrayOfSequence: [Int] = inputOfArray.split(separator: " ").compactMap { Int($0) }
    
        // [Int] maxSum (mutable): Integer that stores the max continuos sum
        var maxSum: Int = arrayOfSequence[0]
        
        // [Int] currentSum (mutable): Integer that selects number in now index or continuos sum to select maxSum
        var currentSum: Int = arrayOfSequence[0]
        
        for i in 1..<n {
            // Update currentSum by choosing a larger value between now number and continuos sum
            if let current: Int = [arrayOfSequence[i], currentSum + arrayOfSequence[i]].max() {
                currentSum = current
            }
            
            // Update maxSum by choosing a larger value between maxSum and currentSum
            if let max: Int = [maxSum, currentSum].max() {
                maxSum = max
            }
        }
        
        print(maxSum)
    }
}