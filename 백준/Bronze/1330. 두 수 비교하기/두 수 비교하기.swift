let inputArray: [Int] = (readLine() ?? "0 0").split(separator: " ").map{Int($0) ?? 0}

let A: Int = inputArray[0]
let B: Int = inputArray[1]

if (A>B) {
    print(">")
} else if (A<B) {
    print("<")
} else {
    print("==")
}