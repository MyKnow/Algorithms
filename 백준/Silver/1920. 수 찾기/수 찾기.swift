func solution() {
    // N: Int (Not used)
    // description: Number of elements in set A
    guard let inputOfN = readLine(), let _ = Int(inputOfN) else {
        return
    }
    
    // A: Set<Int> (immutable)
    // description: A set containing N unique integers for fast lookup
    guard let inputOfA = readLine() else {
        return
    }
    let A: Set<Int> = Set(inputOfA.split(separator: " ").compactMap{ Int($0) })
    
    // M: Int (Not used)
    // description: Number of elements in array B
    guard let inputOfM = readLine(), let _ = Int(inputOfM) else {
        return
    }
    
    // B: [Int] (immutable)
    // description: An array of M integers to be searched in set A
    guard let inputOfB = readLine() else {
        return
    }
    let B: [Int] = inputOfB.split(separator: " ").compactMap{ Int($0) }
    
    // result: [String] (mutable)
    // description: An array to store "1" if element exists in A, "0" otherwise
    // initial: empty array
    var result = [String]()
    for b in B {
        result.append(A.contains(b) ? "1" : "0")
    }
    
    // Output all results at once to minimize I/O overhead
    print(result.joined(separator: "\n"))
}

solution()