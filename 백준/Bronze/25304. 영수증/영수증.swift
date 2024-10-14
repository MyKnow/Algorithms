// X : 영수증에 적힌 총 금액
let X: Int = Int(readLine() ?? "1") ?? 1

// N : 구매한 물건의 종류의 수
let N: Int = Int(readLine() ?? "1") ?? 1

var result : Int = 0
for _ in 0..<N {
    let inputArray: [Int] = readLine()?.split(separator: " ").compactMap { Int($0) } ?? [1, 1]
    
    if (inputArray.count == 2) {
        result += (inputArray[0] * inputArray[1])
    }
}

if (X == result) {
    print("Yes")
} else {
    print("No")
}