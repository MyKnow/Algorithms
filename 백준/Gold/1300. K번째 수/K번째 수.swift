if let inputOfN: String = readLine(), let N: Int = Int(inputOfN),
    let inputOfK: String = readLine(), let K: Int = Int(inputOfK) {
        
    // Index starts at 1
    var start: Int = 1

    // Kth number isn't be bigger than K
    var end: Int = K

    while (start <= end) {
        let mid: Int = (start+end) / 2

        // Count of numbers less than "mid" in list B
        var total: Int = 0
    
        for i in 1...N {
            // mid / i : Column index smaller than "mid" value in row i
            total += min(mid / i, N)
        }
    
        // When "mid" smaller than B[K]
        if total < K {
            start = mid + 1
        }
        else {
            end = mid - 1
        }
    }
        
    print(start)   
}