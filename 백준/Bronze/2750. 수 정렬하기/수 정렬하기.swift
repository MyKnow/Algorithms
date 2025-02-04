// [Int] N (immutable): 숫자 개수 (범위(자연수): 1 <= N <= 1,000))
let N: Int = Int(readLine() ?? "1") ?? 1

// [Array<Int>] arrayOfNumbers (immutable): 입력된 숫자를 저장한 배열 (길이: N)
var arrayOfNumbers: Array<Int> = [Int]()

for _ in 0..<N {
    arrayOfNumbers.append(Int(readLine() ?? "1") ?? 1)
}

print(arrayOfNumbers.sorted().map { String($0) }.joined(separator: "\n"))