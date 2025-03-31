if let input: String = readLine() {
    let arrayOfInput: [Int] = input.split(separator: " ").compactMap { Int($0) }
    
    // N: Int (immutable)
    // description: An integer representing total number of days that temperature was 
    // range: 2 ≤ N ≤ 100,000
    let N: Int = arrayOfInput[0]
    
    // K: Int (immutable)
    // description: An integer representing number of consecutive days to obtain a sum
    // range: 1 ≤ K ≤ N
    let K: Int = arrayOfInput[1]

    if let line: String = readLine() {
        // temps: [Int] (immutable)
        // description: An array of integers that stores the measured temperatures for each day
        // range: -100 ≤ temps ≤ 100
        // length: N
        let temps: [Int] = line.split(separator: " ").compactMap { Int($0) }

        // pSum: [Int] (mutable)
        // description: An array of integers to calculate prefix sum of temps
        // length: N
        var pSum = [Int]()
        
        // Calculate prefix sum
        for num in temps {    
            if let last: Int = pSum.last {
                pSum.append( last+num )
            } else {
                pSum.append( num )
            }
        }

        
        // maxValue: Int (mutable)
        // description: An integer to find the greatest sum in each esction of the pSum
        // initial: min(temps) * max(N)
        var maxValue: Int = -100*100_000
        
        // from K-1: Start from first sum of section
        // to N: Proceed to the last sum of sections.
        for idx in K-1..<N {
            // sumOfSection: Int (immutable)
            // description: An integer representing the sum of K-number intervals 
            // from idx-K to idx of pSum 
            let sumOfSection: Int = pSum[idx] - (idx-K >= 0 ? pSum[idx-K] : 0)
            
            // Update maxValue
            maxValue = max(maxValue, sumOfSection)
            
        }
        
        // Print answer
        print(maxValue)
    }
}