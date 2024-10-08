let numberArray: [Int] = (readLine() ?? "1 1 1").split(separator: " ").map{Int($0) ?? 1}

print(numberArray.reduce(0, +))