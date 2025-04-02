// S: String (immutable)
// description: A string to solve problem
// lenght: ≤ 200,000
// restriction: only lowercase
//
// q: int (Not used)
// description: A integer representing number of queries
// range: 1 ≤ q ≤ 200,000
if let S: String = readLine(), let qOfInput = readLine(), let _: Int = Int(qOfInput) {
    // pSum: [[Int]] (mutable)
    // description: 2-Dimensional array of integer to calculate a prefix sum of each alphabet count
    // length: S.count * 26
    var pSum = [[Int]](
        repeating: [Int](
            repeating: 0,
            count: S.count
        ),
        count: 26
    )

    for (i, c) in S.enumerated() {
        // idx: UInt8 (immutable)
        // description: Index of the alphabet "S[i]" in the range from 0 to 25
        if let ascii: UInt8 = c.asciiValue {
            let idx: Int = Int(ascii)-97
            
            // 1. Update the current index value of the alphabet S[i] 
            // to the previous index value plus 1
            pSum[idx][i] = pSum[idx][max(i-1, 0)] + 1
            
            // 2. Update other alphabet to the previous index value
            for j in 0..<26 {
                // Except current alphabet
                if j != idx {
                    pSum[j][i] = pSum[j][max(0, i-1)]
                }
            }
        }
    }
    
    // results: [String] (mutable)
    // description: A array of strings to store each query's answer for quick output
    // length: q
    var results = [String]()

    // queries: String
    // description: A array of String that store queries that include alphabet and range
    // range: 0 ≤ l ≤ r < len(S)
    // restriction: c is given in lowercase only.
    while let query: String = readLine() {
        let arrayOfQuery: [String] = query.split(separator: " ").map { String($0) }
        
        // Split queries to c, l, r
        // c: current alphabet
        // l, r: range for finding c
        let c: Character = Character(arrayOfQuery[0])
        if let ascii: UInt8 = c.asciiValue, 
            let l: Int = Int(String(arrayOfQuery[1])), 
            let r: Int = Int(String(arrayOfQuery[2])) {
                
            let cIdx: Int = Int(ascii)-97
            // Obtain a number of c in range [l, r] and Append to results
            results.append(String(pSum[cIdx][r] - (l-1 < 0 ? 0 : pSum[cIdx][l-1]) ))
        }
    }
    
    // Print answer
    print(results.joined(separator: "\n"))
}