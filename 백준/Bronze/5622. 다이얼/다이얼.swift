// [String] word (immutable) : 알파벳 대문자로 이루어진 단어 (길이: 2 <= len <= 15)
let word: String = readLine() ?? "WA"

// [UInt8] sumOfTime (mutable) : 다이얼을 돌린 총 시간
var sumOfTime: UInt8 = 0

// [UInt8] minTimeForInput (immutable) : 다이얼을 돌리는 데 필요한 최소 시간
let minTimeForInput: UInt8 = 2

// 문자열을 순회하며 소요되는 시간을 모두 합한다.
for alphabet in word {
    // [UInt8] alphabetInAscii (immutable) : 아스키코드에서의 alphabet
    let alphabetInAscii: UInt8 = alphabet.asciiValue ?? 1
    
    // 7번, 9번 다이얼은 알파벳이 4개 들어있으므로, 이를 처리하는 조건문을 생성함.
    if (alphabetInAscii < (Character("P").asciiValue ?? 1)) {
        // 알파벳 인덱스 차이에서 3을 나눈 몫을 최소 소요 시간과 더한 값을 이용한다.
        sumOfTime += minTimeForInput + 1 + (alphabetInAscii - (Character("A").asciiValue ?? 1)) / 3
    }
    else if (alphabetInAscii <= (Character("S").asciiValue ?? 1)) {
        // P, Q, R, S 중 하나이므로 고정된 값을 더한다.
        sumOfTime += minTimeForInput + 6
    }
    else if (alphabetInAscii < (Character("W").asciiValue ?? 1)) {
        // T, U, V 중 하나이므로 고정된 값을 더한다.
        sumOfTime += minTimeForInput + 7
    }
    else {
        // W, X, Y, Z 중 하나이므로 고정된 값을 더한다.
        sumOfTime += minTimeForInput + 8
    }
}
// sumOfTime 출력
print(sumOfTime)