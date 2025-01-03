// T: Int (immutable)- 테스트 케이스의 개수 (1 <= T <= 10)
let T: Int = Int(readLine() ?? "1") ?? 1

for _ in 0..<T {
    // word: String (immutable) - 알파벳 대문자로만 이루어진 문자열 (길이: <1000)
    let word: String = readLine() ?? ""
    
    // 첫 번째와 마지막 문자를 추출하고 문자열로 변환하여 연결
    let firstCharacter: String = String(word[word.startIndex])
    let lastCharacter: String = String(word[word.index(before: word.endIndex)])
    
    print(firstCharacter + lastCharacter)
}