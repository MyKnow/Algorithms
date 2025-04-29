func binarySearch(_ target: Int, _ lst: inout [Int]) -> Int {
    var start: Int = 0
    
    guard let max: Int = lst.max() else {
        return -1
    }
    var end: Int = max

    while(start <= end) {
        let mid: Int = (start+end) / 2

        var total = 0
        for h in lst {
            if h > mid {
                total += (h - mid)
            }
        }

        if total >= target {            
            start = mid + 1
        }
        else {
            end = mid - 1
        }
    }

    return end
}

if let inputOfNM: String = readLine(), let inputOfTrees: String = readLine() {
    let arrayOfNM: [Int] = inputOfNM.split(separator: " ").compactMap { Int($0) }
    let (_, M): (Int, Int) = (arrayOfNM[0], arrayOfNM[1])

    var trees: [Int] = inputOfTrees.split(separator: " ").compactMap { Int($0) }
    
    print(binarySearch(M, &trees))
}