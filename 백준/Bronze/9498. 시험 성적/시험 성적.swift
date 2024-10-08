let score: Int = Int(readLine() ?? "0") ?? 0

if (90 <= score) {
    print("A")
} else if (80 <= score) {
    print("B")
} else if (70 <= score) {
    print("C")
} else if (60 <= score) {
    print("D")
} else {
    print("F")
}