let inputArray: [Int] = (readLine() ?? "2 2 2").split(separator: " ").map{Int($0) ?? 2}

let A: Int = inputArray[0]
let B: Int = inputArray[1]
let C: Int = inputArray[2]

print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)