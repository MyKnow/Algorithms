if let inputNM: String = readLine() {
    let arrayOfNM: [Int] = inputNM.split(separator: " ").compactMap { Int($0) }

    // N: int (immutable)
    // description: An integer representing count of numbers
    // range: 1 ≤ N ≤ 1_000_000
    let N: Int = arrayOfNM[0]

    // M: int (immutable)
    // description: An integer that divides the sum of consecutive intervals so that the remainder becomes zero.
    // range: 2 ≤ M ≤ 1,000
    let M: Int = arrayOfNM[1]

    if let inputA: String = readLine() {
        // A: [Int] (immutable)
        // description: A list of integers that stores the Nth number to obtain the number of intervals 
        // whose remainder is zero when the sum of consecutive intervals is divided by M
        // range: 0 ≤ A_i ≤ 10^9
        // length: N
        let A: [Int] = inputA.split(separator: " ").compactMap { Int($0) }

        // remainders: [Int] (mutable)
        // description: A list of integers to store remainders of A's prefix sum divided by M
        // length: M
        var remainders = [Int](
            repeating: 0,
            count: M
        )
        
        // pSum: Int (mutable)
        // description: An integer to store A's current prefix sum
        // initial: 0
        var pSum: Int = 0
        
        // count: Int
        // description: An integer to store number of intervals 
        // whose remainder is zero when the sum of consecutive intervals is divided by M
        var count: Int = 0
        
        for i in 0..<N {
            // Update the pSum to the previous pSum + current number of A
            pSum += A[i]
        
            // Obtain remainder between pSum and M
            let remainder: Int = pSum % M
        
            // Increase the count when remainder is 0
            if remainder == 0 {
                count += 1
            }
        
            // Increase the remainders of current index
            remainders[remainder] += 1
        }
        
        // Update the count variable with the remaining number stored in "remainers".
        // r * (r-1) / 2: number of consecutive intervals
        for r in remainders {
            count += r * (r-1) / 2
        }
        
        // Print answer
        print(count)
    }
}