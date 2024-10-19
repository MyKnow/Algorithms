// N: Number of rows of stars
let N: Int = Int(readLine() ?? "1") ?? 1

for i in 1...N {
    for j in 0..<i {
        print("*", terminator: "")
    }
    print()
}