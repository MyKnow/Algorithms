// N: The Number of rows of stars
let N: Int = Int(readLine() ?? "1") ?? 1

for i in 1...N {
    for _ in 0..<N-i {
        print(" ", terminator: "")
    }
    for _ in 0..<i {
        print("*", terminator: "")
    }
    print()
}