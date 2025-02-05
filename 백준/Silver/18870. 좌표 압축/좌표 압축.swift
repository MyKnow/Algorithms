let _ = Int(readLine() ?? "1") ?? 1

// [Array<Int>] arrayOfPoints (immutable): 입력 받은 좌표를 저장하는 배열 (길이: N)
let arrayOfPoints: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }

// [Array<Int>] arrayWithoutDuplicate (immutable): 중복을 제거하여 정렬한 배열 (길이: <= N)
let arrayWithoutDuplicate: Array<Int> = Array(Set(arrayOfPoints)).sorted()

// [Dictionary<Int>] dictOfPoints (mutable): 입력 받은 좌표를 압축한 사전 (길이: arrayWithoutDuplicate.count))
var dictOfPoints: Dictionary<Int, Int> = Dictionary<Int, Int>()

for (index, value) in arrayWithoutDuplicate.enumerated() {
    dictOfPoints[value] = index
}

// number를 dictOfPoints에서 찾아내어 출력한다.
print(arrayOfPoints.map { String(dictOfPoints[$0] ?? 0)}.joined(separator: " "))