// Binary search function
// Return lower bound index of target in "lst"
func binarySearch(_ lst: [Int], _ target: Int) -> Int {
    var start: Int = 0
    var end: Int = lst.count

    while (start < end) {
        let mid: Int = (start+end) / 2

        // Lower bound
        if (lst[mid] < target) {
            start = mid + 1
        }
        else {
            end = mid
        }
    }

    return start
}

if let inputOfN: String = readLine(), let _: Int = Int(inputOfN),
    let inputOfA: String = readLine() {
    let A: [Int] = inputOfA.split(separator: " ").compactMap { Int($0) }
        
    // A list to calculate length of LIS
    // Does not guarantee that LIS is saved.
    var LIS = [Int]()

    for a in A {
        let idx: Int = binarySearch(LIS, a)

        // Append "a" to the LIS when maximum value of the LIS is less than "a"
        if idx == LIS.count {
            LIS.append(a)
        }
        // The process of replacing with a smaller value
        else {
            LIS[idx] = a
        }
    }
    
    print(LIS.count)
}