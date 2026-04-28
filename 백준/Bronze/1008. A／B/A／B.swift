let array: [Int] = (readLine() ?? "1 1").split(separator: " ").map{ Int($0) ?? 1}
let doubleResult: Double = Double(array[0]) / Double(array[1])
print(doubleResult)