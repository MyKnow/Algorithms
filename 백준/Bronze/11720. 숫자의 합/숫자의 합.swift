// [Int] N (immutable) : 입력할 숫자의 갯수 (1 <= N <= 100)
let N: Int = Int(readLine() ?? "1") ?? 1

// [String] numbers (immutable) : 공백 없이 연결된 숫자들의 문자열 (길이: N)
let numbers: String = readLine() ?? "0"

// [Int] sumOfNumbers (mutable) : 숫자들의 총 합계
var sumOfNumbers: Int = 0

// for문으로 numbers를 number로 분리하여 sumOfNumbers에 더한다.
for number in numbers {
    sumOfNumbers += Int(String(number)) ?? 0
}

// sumOfNumbers 출력
print(sumOfNumbers)