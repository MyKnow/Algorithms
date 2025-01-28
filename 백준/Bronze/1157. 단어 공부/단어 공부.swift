// [String] word (immutable): 알파벳 대소문자로 이루어진 단어 (길이: < 1,000,000)
let word: String = readLine() ?? "a"

// [String] upperWord (immutable): 알파벳 대문자로만 이루어진 word
let upperWord: String = word.uppercased()

// [Dictionary<String, Int>] (mutable) alphabetDict : upperWord에서 발견된 alphabet과 발견된 횟수를 저장하는 사전
var alphabetDict = Dictionary<String, Int>()

// upperWord 순회
for alphabet in upperWord {
    // 이미 alphabetDict에 해당 alphabet이 존재한다면 횟수 업데이트
    if let count = alphabetDict[String(alphabet)] {
        alphabetDict[String(alphabet)] = count + 1
    } else {
        alphabetDict[String(alphabet)] = 1
    }
}
// [Array<String>] mostFoundedAlphabetArray (immutable): 최빈값에 해당하는 알파벳 리스트
let mostFoundedAlphabetArray: Array<String> = alphabetDict.filter {$0.value == alphabetDict.values.max() ?? 0}.map { $0.key }

// mostFoundedAlphabetArray 길이가 2 이상이면 ?를 출력한다.
print(mostFoundedAlphabetArray.count > 1 ? "?" : mostFoundedAlphabetArray[0])