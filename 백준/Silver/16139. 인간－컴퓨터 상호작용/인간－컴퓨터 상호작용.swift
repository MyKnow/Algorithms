import Foundation

if let S = readLine(), let _ = readLine() {
    let n = S.count
    let chars = Array(S.utf8) // ASCII 변환을 위해 Array로 변환
    var pSum = Array(repeating: [Int](repeating: 0, count: n), count: 26)

    pSum[Int(chars[0]) - 97][0] = 1 // 첫 번째 문자 초기화

    for i in 1..<n {
        let idx = Int(chars[i]) - 97
        for j in 0..<26 {
            pSum[j][i] = pSum[j][i-1] + (j == idx ? 1 : 0)
        }
    }

    var results = [String]()

    while let query = readLine() {
        let parts = query.split(separator: " ")
        let cIdx = Int(parts[0].utf8.first!) - 97
        let l = Int(parts[1])!
        let r = Int(parts[2])!

        results.append(String(pSum[cIdx][r] - (l > 0 ? pSum[cIdx][l-1] : 0)))
    }

    print(results.joined(separator: "\n"))
}