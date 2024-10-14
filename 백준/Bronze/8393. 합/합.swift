let n: Int = Int(readLine() ?? "1") ?? 1

var result: Int = 0
for i in 1...n {
    result += i
}

print(result)