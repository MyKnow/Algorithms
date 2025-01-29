// [Int] N (immutable): 단어의 개수 (1 <= N <= 100)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Int] count (mutable): 발견된 그룹 단어의 개수
var count: Int = 0

for _ in 0..<N {
    // [Array<String>] stackOfAlphabet (mutable) : 입력된 단어의 알파벳을 순서대로 저장하는 스택
    var stackOfAlphabet: Array<String> = Array<String>()
    
    // [String] word (immutable) : 알파벳 소문자로만 이루어진 입력한 단어 (길이: <= 100)
    let word: String = readLine() ?? "a"
    
    for index in 0..<word.count {
        // [String.Index] idx : word의 index번째 인덱스
        let idx: String.Index = word.index(word.startIndex, offsetBy: index)
        // [String] alphabetOfNowIndex (immutable) : 현재 인덱스의 알파벳
        let alphabetOfNowIndex: String = String(word[idx])
        
        // 만약 스택 안에 해당 알파벳이 없다면 추가한다.
        if (!stackOfAlphabet.contains(alphabetOfNowIndex)) {
            stackOfAlphabet.append(alphabetOfNowIndex)
        }
        // 스택 안에 해당 알파벳이 존재하는데, Top에 위치하지 않다면 그룹 단어가 아니다.
        else if (stackOfAlphabet.last != alphabetOfNowIndex) {                
            break
        }
                
        // 마지막 인덱스까지 검사했는데도 이상이 없다면 count를 증가한다.
        if (index == word.count-1) {
            count += 1
        }
    } 
}
// count 출력
print(count)