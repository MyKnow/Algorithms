import Foundation

// [func([[Int, Int]]) -> Int] getLIS
// : A function that finds the LIS length from a list of tuples
//
// - Parameters:
// 1. A: [(Int, Int)]
// description: A list of tuples storing electric wires connected to A and B poles
//
// - Returns:
// 1. dp.count: Int
// description: The length of LIS obtained from the list
func getLIS(_ A: [(Int, Int)]) -> Int {
    // dp: [Int]
    // description: List of integers to store positions of wires from pole B
    var dp: [Int] = []
    
    for i in 0..<A.count {
        // idx: Int
        // Index indicating where the wire can be inserted now
        let idx = dp.binarySearch(A[i].1)

        // When idx is the last index
        if idx == dp.count {
            // Just append it
            dp.append(A[i].1)
        } else {
            // Update already existing elements
            dp[idx] = A[i].1
        }
    }
    
    return dp.count
}

// Extension for Array to find lower bound index (equivalent to bisect.bisect_left)
extension Array where Element: Comparable {
    func binarySearch(_ target: Element) -> Int {
        var left = 0, right = self.count
        while left < right {
            let mid = (left + right) / 2
            if self[mid] < target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
}

// N: Int
// description: An integer that represents the number of electric wires
if let input: String = readLine(), let N: Int = Int(input) {

    // wires: [(Int, Int)]
    // description: A list of tuples storing electric wires connected to A and B poles
    var wires = [(Int, Int)]()
    
    // Update wires
    while let lines = readLine() {
        let line: [Int] = lines.split(separator: " ").compactMap { Int($0) }
        wires.append( (line[0], line[1]) )
    }
    
    // Sort in ascending order by pole A
    wires.sort { $0.0 < $1.0 }
    
    // Get length of LIS of wires
    let lengthOfLIS: Int = getLIS(wires)
    
    // Print result
    print(N - lengthOfLIS)
}