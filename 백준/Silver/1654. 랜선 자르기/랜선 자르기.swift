// binarySearch: func(Int, [Int]) -> Int
// description: A function that returns the length of the maximum 
// cable that can make n cables on a given cable
// 
// Parameters
// n: Int -> Number of targets to divide cable
// lst: [Int] -> Length of each cables array
//
// Return
// best: Int -> Longest cable length divided Into n cables
func binarySearch(_ n: Int, _ lst: [Int]) -> Int {
    // start: Int (mutable)
    // minimum length of cable
    // initial: 1
    var start: Int = 1
    
    guard let lastOfLst: Int = lst.last else {
        return -1
    }
    // end: Int (mutable)
    // maximum length of cable
    // initial: longest length of lst (lastOfLst)
    var end: Int = lastOfLst

    // best: Int (mutable)
    // An integer that stores the longest cable divided Into n cables
    // initial: 0
    var best: Int = 0

    // Binary Search
    while(start<=end) {
        // mid: Int (immutable)
        let mid: Int = (start+end) / 2

        // numberOfCable: Int (mutable)
        // description: An integer to store the number of cables divided by "mid" length
        // initial: 0
        var numberOfCable: Int = 0
        for l in lst {
            numberOfCable += (l / mid)
        }

        // When numberOfCable is bigger than number of target
        if numberOfCable >= n {
            // Update best by mid
            best = mid

            // Increase length of cable by mid + 1
            start = mid + 1
        }
        else {
            // Decrease length of cable by mid - 1
            end = mid - 1
        }
    }

    return best
    
}
    
if let inputOfKN: String = readLine() {
    let arrayOfKN: [Int] = inputOfKN.split(separator: " ").compactMap { Int($0) }
    // K: Int (immutable)
    // description: An integer that represents number of cables that already have
    var K: Int = arrayOfKN[0]
    
    // N: Int
    // description: An integer that represents number of cables required
    let N: Int = arrayOfKN[1]

    // lenghts: [Int] (mutable)
    // description: An array of integers that stores length of each cables
    var lengths = [Int]()
    while let line: String = readLine(), let length = Int(line), K != 0 {
        lengths.append( length )
        K -= 1
    }
    
    // Sort of "lengths" for binary search
    lengths.sort()
    
    // Print result of binarySearch
    print(binarySearch(N, lengths))
}