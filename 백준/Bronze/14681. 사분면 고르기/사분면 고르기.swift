let x = Int(readLine() ?? "1") ?? 1
let y = Int(readLine() ?? "1") ?? 1

if (y > 0) {
    if (x > 0) {
        print(1)
    } else {
        print(2)
    }
} else {
    if (x < 0) {
        print(3)
    } else {
        print(4)
    }
}