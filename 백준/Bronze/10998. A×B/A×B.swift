let number: [Int] = (readLine() ?? "1 1").split(separator: " ").map{Int($0) ?? 1}

print(number[0] * number[1])
