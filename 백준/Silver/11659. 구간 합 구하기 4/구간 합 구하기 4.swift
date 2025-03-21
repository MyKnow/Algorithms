if let input: String = readLine() {
    let arrayOfInput = input.split(separator: " ").compactMap {Int($0)}
    // [Int] _ (Disabled): An Integer that represents length of mapOfN (range: 1 ≤ N ≤ 100,000)
    // [Int] M (immutuable): An Integer that represents count of test cases (range: 1 ≤ M ≤ 100,000)
    let (_, M): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

    // [Array<Int>] arrayOfN (immutable): Array of Integers that stores nature numbers to find prefix sum
    let arrayOfN: [Int] = (readLine() ?? "1").split(separator: " ").compactMap {Int($0)}
    
    // [Array<Int>] prefixSum (mutable): Array of Integers that stores prefix sum of mapOfN
    var prefixSum: [Int] = [0]
    
    // Update prefixSum
    for (idx, n) in arrayOfN.enumerated() {
        prefixSum.append( n + prefixSum[idx] )
    }
    
    for _ in 0..<M {
        // [Int] i, j (immutable): An integer representing the range to obtain the prefix sum (range: 1 ≤ i ≤ j ≤ N)
        let line: [Int] = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
        let (i, j): (Int, Int) = (line[0], line[1])
    
        // Calculate sum of sections i to j
        print(prefixSum[j] - prefixSum[i-1])
    }
}