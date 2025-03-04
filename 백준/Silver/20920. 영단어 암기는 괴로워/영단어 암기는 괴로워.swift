// [Int] N, M (immutable)
// N: 단어의 수, (범위(자연수): 1 ≤ N ≤ 100,000)
// M: 단어 길이 제한, (범위(자연수): 1 ≤ M ≤ 10)
let arrayOfInput: [Int] = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
let (N, M): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

// [Dictionary[String: Int]] words (mutable): 길이가 M 이상인 단어를 저장하는 사전 (단어: 빈도 수)
var words: [String: Int] = [:]

for _ in 0..<N {
        // M보다 짧은 길이의 단어는 고려하지 않는다.
    if let word: String = readLine(), word.count >= M {
       words[word, default: 0] += 1 
    }
}
    
let sortedWords = words.sorted {
    // 1. 빈도 수 내림차순
    if $0.value != $1.value { return $0.value > $1.value }  
    
    // 2. 길이 내림차순
    if $0.key.count != $1.key.count { return $0.key.count > $1.key.count } 
    
    // 3. 알파벳 오름차순
    return $0.key < $1.key 
}
    
// 결과 출력
print(sortedWords.map { $0.key }.joined(separator: "\n"))