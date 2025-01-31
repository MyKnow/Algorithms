// pow를 사용하기 위한 Foundation Import
import Foundation

// [Array<String>] inputOfProblem (immutable): 문제의 입력을 분리 저장한 배열
let inputOfProblem: Array<String> = (readLine() ?? "0 2").split(separator: " ").map { String($0) }

// [String] N (immutable): B진법 수 
let N: String = inputOfProblem[0]

// [Int] B (immutable): 진법 수 (2 <= B <= 36)
let B: Int = Int(inputOfProblem[1]) ?? 2


// [Int] sumOfN (mutable): 10진법으로 변환한 N (10진법으로 변환한 크기: <=100,000,000)
// A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35 진법
var sumOfN: Int = 0

func asciiValue(_ c: Character) -> Int {
    return Int(c.asciiValue ?? 65)
}

// 문자열 N을 순회하며 계산
for i in 0..<N.count {
    // [Character] n: N 문자열의 앞에서 i번째 문자
    let indexOfN: String.Index = N.index(N.startIndex, offsetBy: i)
    let n: Character = N[indexOfN]

    // [Int] converted (immutable): 변환된 자리수
    let converted: Int
    
    // 문자인 경우 변환 필요
    if (n.isLetter) {
        converted = (asciiValue(n)-asciiValue("A")+10)
    }
    else {
        converted = Int(String(n)) ?? 0
    }
    // (변환된 수) * (진법**자리)
    sumOfN += converted * Int(pow(Double(B), Double(N.count-i-1)))
}

// 출력
print(sumOfN)