import Foundation

// [func(Int) -> String] cantor: N에 대한 칸토어 집합의 근사를 출력하는 함수
func cantor(_ target: Int) -> String {
    // target이 0인 경우 그냥 - 만 출력
    if target == 0 {
        return "-"
    } else {
        // 조건에 맞춰 문자열 생성
        let line = cantor(target - 1)
        let blank = String(repeating: " ", count: Int(pow(3, Double(target-1))))
        return line + blank + line
    }
}

// [Int] N: 칸토어 집합의 근사를 만들 길이 (범위(정수): 0 <= N <= 12)
while let input: String = readLine(), let N: Int = Int(input) {
    print(cantor(N))
}