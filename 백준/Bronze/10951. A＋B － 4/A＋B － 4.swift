while true {
    // inputArray: Array<Int> to be used for Addition
    let inputArray: [Int] = readLine()?.split(separator: " ").compactMap{Int($0)} ?? [-1, -1]
    
    // 0 < A, B < 10
    let A: Int = inputArray[0]
    let B: Int = inputArray[1]
    
    if (A == -1 || B == -1) {
        break
    } else {
        print(A+B)
    }
}