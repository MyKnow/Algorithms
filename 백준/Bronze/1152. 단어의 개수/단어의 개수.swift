// trimmingCharacters 함수 사용을 위해 import 함
import Foundation

// [String] S (immutable) : 영어 대소문자와 공백으로 이루어진 문자열 (길이: < 1,000,000)
let S: String = readLine() ?? ""

// [String] stringWithStrip (immutable) : 양쪽 공백을 trimmingCharacters 함수로 지운 문자열
let stringWithStrip: String = S.trimmingCharacters(in: [" "])

// 만약 stringWithStrip의 결과가 빈 문자열이라면, 0으로 처리한다.
if (stringWithStrip == "") {
    print(0)
}
else {
    // 공백을 기준으로 문자열을 나누어 Array에 넣고, 해당 Array의 길이를 출력한다.
    // [Array<String>] arrayOfWords (immutable) : 문자열에서 추출한 단어들을 담은 Array
    let arrayOfWords: Array<String> = stringWithStrip.split(separator: " ").map(String.init)

    // Array의 길이를 출력한다.
    print(arrayOfWords.count)
}