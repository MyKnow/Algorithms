let number: [Int] = (readLine() ?? "1 1").split(separator: " ").map{Int($0) ?? 1}

let n1: Int = number[0]
let n2: Int = number[1]

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1%n2)