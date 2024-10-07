let input = (readLine() ?? "0 0").split(separator: " ").map{(Int($0) ?? 0)}

print(input[0] + input[1])