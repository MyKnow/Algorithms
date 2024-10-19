while true {
    // inputArray: Array<Int> to be used for Addition
    let inputArray: [Int] = readLine()?.split(separator: " ").compactMap{Int($0)} ?? [0, 0]
    
    // 0 <= A, B < 10
    let A: Int = inputArray[0]
    let B: Int = inputArray[1]
    
    if (A == 0 && B == 0) {
        break
    } else {
        print(A+B)
    }
}