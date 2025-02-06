// [Int] N(immutable): 상근이가 가지고 있는 숫자 카드의 개수 (범위(자연수): 1 ≤ N ≤ 500,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Set<Int>] setOfCards (immutable): 상근이가 가지고 있는 카드를 저장하는 집합 (크기: N)
let setOfCards: Set<Int> = Set<Int>((readLine() ?? "1").split(separator: " ").compactMap { Int($0) })

// [Int] M (immutable): 입력될 정수의 개수 (범위(자연수): 1 ≤ M ≤ 500,000)
let M: Int = Int(readLine() ?? "1") ?? 1

// [Array<Int>] listOfNumbers (immutable): 입력 받은 숫자를 저장하는 배열 (크기: N)
let listOfNumbers: Array<Int> = Array<Int>((readLine() ?? "1").split(separator: " ").compactMap { Int($0) })

// [Array<String>] result (mutable): 출력할 문자열을 저장하는 배열
var result: [String] = [String]()
for number in listOfNumbers {
    if (setOfCards.contains(number)) {
        result.append("1")
    }
    else {
        result.append("0")
    }
}
        
print(result.joined(separator: " "))