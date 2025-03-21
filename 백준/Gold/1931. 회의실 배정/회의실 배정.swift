// [Int] N (immutable): An Integer that represents number of meeting(range: 1 ≤ N ≤ 100,000)
if let input: String = readLine(), let N: Int = Int(input) {
    // [Int] lastEnd (mutable): An Integer that stores last meeting time
    var lastEnd: Int = 0
    
    // [int] count (mutable): An Integer that stores the number of meetings
    var count: Int = 0
    
    // [Array<Array<Int>>] arrayOfTimes (mutable): 2-Dimensional arrya of integers that 
    // stores start and end time of each meetings
    var arrayOfTimes = [[Int]]()
    
    for _ in 0..<N {
        let times: [Int] = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
        arrayOfTimes.append( times )
    }
    
    // Sort by end time of meetings
    arrayOfTimes.sort { $0[1] == $1[1] ? $0[0] < $1[0] : $0[1] < $1[1] }
    
    for times in arrayOfTimes {
        // [Int] start, end (immutable): Start and end times of the now meeting
        let (start, end): (Int, Int) = (times[0], times[1])
        
        // Update count and lastEnd when start is later than or equal to lastEnd
        if (start >= lastEnd) {
            count += 1
            lastEnd = end
        }
    }
    print(count)
}