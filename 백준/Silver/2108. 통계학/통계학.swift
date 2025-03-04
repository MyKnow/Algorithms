import Foundation

// [Int] N (immutable): 수의 개수 (범위: 1 ≤ N ≤ 500,000)
let N = Int(readLine()!)!

// [Array<Int>] numbers: 입력된 수 저장
var numbers = [Int]()
var sumOfNumbers = 0

// [Dictionary<Int, Int>] freqDict: 최빈값 계산용 딕셔너리
var freqDict = [Int: Int]()

for _ in 0..<N {
    let num = Int(readLine()!)!
    numbers.append(num)
    sumOfNumbers += num
    freqDict[num, default: 0] += 1
}

// 1. 산술평균 (소수점 첫째 자리 반올림)
print(Int(round(Double(sumOfNumbers) / Double(N))))

// 2. 중앙값 (정렬 후 중간값)
numbers.sort()
print(numbers[N / 2])

// 3. 최빈값 찾기
let maxFrequency = freqDict.values.max() ?? 0
let modes = freqDict.filter { $0.value == maxFrequency }.keys.sorted()

// 최빈값이 여러 개라면 두 번째로 작은 값 선택
print(modes.count > 1 ? modes[1] : modes[0])

// 4. 범위 (최대값 - 최소값)
if let last: Int = numbers.last, let first: Int = numbers.first {
    print(last - first)
}