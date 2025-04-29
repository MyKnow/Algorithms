// * Parameters
// - target: Int -> Number of router to want install
// - arr: [Int] -> Coordinates of each houses (Sorted in ascending order)
//
// * Return
// - end: Int -> Maximum distance between two neighboring router
func binarySearch(_ target: Int, _ arr: [Int]) -> Int {
    // Minimum distance is 1
    var start: Int = 1
    
    // Maximum distance is distance between last and first
    guard let last: Int = arr.last, let first = arr.first else {
        return -1
    }
    var end: Int = last - first

    while(start <= end) {
        let mid: Int = (start+end) / 2

        // Position of last house where the router was installed
        var lastPoint: Int = arr[0]

        // Number of house where router is installed
        // initial: 1 (installed in lastPoint)
        var count: Int = 1

        for idx in 1..<arr.count {
            let crtPoint: Int = arr[idx]

            // When distance between the previous house and 
            // the current house is same to "mid" or greater
            if crtPoint - lastPoint >= mid {
                lastPoint = crtPoint
                count += 1
            }
        }

        if target <= count {
            start = mid + 1
        }
        else {
            end = mid - 1
        }
    }
            
    return end
}

if let inputOfNC: String = readLine() {
    let arrayOfNC: [Int] = inputOfNC.split(separator: " ").compactMap { Int($0) }
    var (N, C): (Int, Int) = (arrayOfNC[0], arrayOfNC[1])

    var X = [Int]()
    while let line: String = readLine(), let point: Int = Int(line), N != 0 {
        X.append( point )
        N -= 1
    }
    X.sort()

    print(binarySearch(C, X))
}