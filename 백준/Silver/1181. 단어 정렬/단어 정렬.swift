// [Int] N (immutable): 입력 받을 단어의 개수 (범위(자연수): 1 ≤ N ≤ 20,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Set<String>] setOfWords (mutable): 입력 받은 단어들을 중복없이 저장하는 집합 (길이: <= N)
var setOfWords: Set<String> = Set<String>()

for _ in 0..<N {
    setOfWords.insert( (readLine() ?? "a") )
}
                 
// [Array<String>] sortedList (immutable): setOfWords를 길이 짧은 순, 사전 순으로 정렬한 배열
let sortedList: Array<String> = setOfWords.sorted(by: { $0.count == $1.count ? $0 < $1 : $0.count < $1.count } )
    
// sortedList 출력
print(sortedList.joined(separator: "\n"))