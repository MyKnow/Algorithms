if let input: String = readLine() {
    let arrayOfInput: [Int] = input.split(separator: " ").compactMap { Int($0) }
    
    // N: Int (Not used)
    // description: An integer that represents the number of items
    // range: 1 ≤ N ≤ 100
    let _: Int = arrayOfInput[0]
    
    // K: Int (immutable)
    // description: An integer that represents the amount that the "준서" can carry
    // range: 1 ≤ K ≤ 100,000
    let K: Int = arrayOfInput[1]

    // items: [ (Int, Int) ] (mutable)
    // description: An array of (Int, Int) tuple to store (weight, value) pairs
    // length: N
    var items = [(Int, Int)]()
    
    // Append each pairs in items array
    while let line: String = readLine() {
        let arrayOfLine: [Int] = line.split(separator: " ").compactMap { Int($0) }
        
        // W: Int (immutable)
        // description: An integer that represents weight of item
        // range: 1 ≤ W ≤ 100,000
        let W: Int = arrayOfLine[0]
        
        // V: Int (immutable)
        // description: An integer that represents value of item
        // range: 1 ≤ V ≤ 1,000
        let V: Int = arrayOfLine[1]
        
        items.append( (W, V) )
    }
    
    // dp: [Int] (mutable)
    // description: An array of integer to store maximum sum of values at each weight
    // length: K
    var dp = [Int](
        repeating: 0,
        count: K
    )
    
    for (W, V) in items {
        // pRow: [Int] (immutable)
        // description: An array of integer that represents previous dp
        // length: K
        let pRow: [Int] = dp
    
        // Iterate from 1 through K
        // k: current weight
        for k in 1...K {
            // kIndex: index of current weight
            let kIndex: Int = k - 1
            
            // When current weight is bigger and same to item's weight
            if (k >= W) {
                // Update dp[kIndex] to maximum value between
                // pRow[kIndex]: previous value at current weight
                // and
                // V + pRow[max(kIndex-W, 0)]: Sum of values between value of current item and previous item.
                dp[kIndex] = max(pRow[kIndex], V + pRow[max(kIndex-W, 0)])
            }
            else {
                // Update dp[kIndex] to previous value at current weight
                dp[kIndex] = pRow[kIndex]
            }
        }
    }  

    // Print last element of dp
    if let last: Int = dp.last {
        print(last)
    }
}