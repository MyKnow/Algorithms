// T: Number of Test cases
let T: Int = Int(readLine() ?? "1") ?? 1

for i in 1...T {
    // inputArray: Array to be used for addition
    // 0 < A, B < 10
    let inputArray: [Int] = readLine()?.split(separator: " ").compactMap{Int($0)} ?? [1, 1]

    let A: Int = inputArray[0]
    let B: Int = inputArray[1]
    
    print("Case #\(i): \(A+B)")
}