// [Int] N (immutable): 입력 받을 수의 개수 (범위(자연수): 1 <= N <= 1,000,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Array<Int>] arrayOfNumbers (mutable): 입력된 N개의 수를 저장하는 배열 (길이: N)
var arrayOfNumbers: Array<Int> = [Int]()

for _ in 0..<N {
    arrayOfNumbers.append(Int(readLine() ?? "1") ?? 1)
}
// arrayOfNumbers를 정렬한다.
arrayOfNumbers.sort()

// arrayOfNumbers를 출력한다.
print(arrayOfNumbers.map { String($0) }.joined(separator: "\n"))