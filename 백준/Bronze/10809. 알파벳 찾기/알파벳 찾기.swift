// [String] S (immutable) : 알파벳 소문자로만 이루어진 단어 (길이 : <= 100)
let S: String = readLine() ?? "a"

// [Array<Int>] alphabetList (mutable) : 각 알파벳들이 처음 등장하는 위치를 저장하는 리스트 (길이: 26)
var alphabetList: Array<Int> = Array<Int>(repeating: -1, count: 26)

// [Int] nowIndex (mutable) : 현재 index
var nowIndex: Int = 0

// 문자열을 분해하여 한글자씩 수행한다.
for alphabet in S {
    // [Int] indexOfAlphabet (immutable) : alphabet이 몇번째 알파벳인지 계산한 변수 (예시: a -> 0)
    let indexOfAlphabet: Int = Int((alphabet.asciiValue ?? 0) - (Character("a").asciiValue ?? 0)) ?? 0
    
    // alphabetList의 indexOfAlphabet번째 요소가 -1이 아니라면 값을 변경하지 않음
    if (alphabetList[indexOfAlphabet] == -1) {
        // 최초 변경인 경우, 단어의 위치를 list에 기록한다.
        alphabetList[indexOfAlphabet] = nowIndex
    }
       
    // nowIndex에 1을 더한다.
    nowIndex += 1
}

// alphabetList를 출력한다.
for indexOfAlphabet in alphabetList {
    print(indexOfAlphabet, terminator: " ")
}