// [Array<Int>] arrayOfNumbers (immutable): 입력된 숫자를 저장한 배열 (길이: N)
var arrayOfNumbers: Array<Int> = [Int]()

for _ in 0..<5 {
    arrayOfNumbers.append(Int(readLine() ?? "1") ?? 1)
}

// [Array<Int>] sortedArray (immutable): 오름차순 정렬된 배열 (길이: N)
let sortedArray: Array<Int> = arrayOfNumbers.sorted()

print("\(sortedArray.reduce(0, +) / sortedArray.count)\n\(sortedArray[2])")