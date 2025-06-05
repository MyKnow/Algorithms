import Foundation

@inline(__always)
func getAscii(_ c: Character) -> Int {
    return Int(c.asciiValue!) - 64
}

func getPrimaryNumbers(_ length: Int) -> [Int] {
    var result = Set<Int>()
    for i in 1...Int(Double(length).squareRoot()) {
        if length % i == 0 {
            result.insert(i)
            result.insert(length / i)
        }
    }
    return result.sorted()
}

func solution() {
    guard let plainLine = readLine(),
          let cipherLine = readLine() else { return }

    let plain = Array(plainLine)
    let cipher = Array(cipherLine)
    let length = plain.count

    let key: [Int] = zip(plain, cipher).map {
        let d = getAscii($1) - getAscii($0)
        return d > 0 ? d : d + 26
    }

    for p in getPrimaryNumbers(length) {
        let pattern = Array(key[0..<p])
        var isMatch = true

        for (i, k) in key.enumerated() {
            if pattern[i % p] != k {
                isMatch = false
                break
            }
        }

        if isMatch {
            let result = pattern.compactMap { UnicodeScalar($0 + 64) }.map { String($0) }.joined()
            print(result)
            break
        }
    }
}

solution()