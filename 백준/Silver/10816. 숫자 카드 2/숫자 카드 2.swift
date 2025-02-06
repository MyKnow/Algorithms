// [Int] N (immutable): 상근이가 가지고 있는 숫자 카드의 개수 (범위(자연수): 1 ≤ N ≤ 500,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Dictionary<Int, Int>] dictOfCards (mutable): 상근이가 가지고 있는 카드를 저장하는 사전 (크기: N)
var dictOfCards: Dictionary<Int, Int> = [Int: Int]()

// 2번째 줄에 입력 받은 수들을 순회한다.
for number in Array((readLine() ?? "1").split(separator: " ").compactMap { Int($0) }) {
    // 1. dictOfCards에 저장된 카드인 경우
    if let exist = dictOfCards[number] {
        // 카드 개수를 1 증가시킨다.
        dictOfCards[number] = exist+1
    }
    // 2. 저장되지 않은 카드인 경우
    else {
        // 새로 등록한다.
        dictOfCards[number] = 1
    }
}

// [Int] M (immutable): 입력될 정수의 개수 (범위(자연수): 1 ≤ M ≤ 500,000)
let M: Int = Int(readLine() ?? "1") ?? 1

// [Array<String>] arrayOfResult (mutable): 출력할 답을 저장하는 배열
var arrayOfResult: Array<String> = [String]()

// 4번째 줄에 입력 받은 수들을 순회한다.
for number in Array((readLine() ?? "1").split(separator: " ").compactMap { Int($0) }) {
    if let exist = dictOfCards[number] {
        arrayOfResult.append(String(exist))
    }
    else {
        arrayOfResult.append("0")
    }
}

// 값 출력
print(arrayOfResult.joined(separator: " "))