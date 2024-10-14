let testCase: Int = Int(readLine() ?? "1") ?? 1

for i in 0..<testCase {
    let inputArray: [Int] = (readLine() ?? "1 1").split(separator: " ").map{ Int($0) ?? 1}
    
    print(inputArray[0] + inputArray[1])
}