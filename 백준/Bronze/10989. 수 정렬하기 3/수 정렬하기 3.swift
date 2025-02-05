import Foundation

final class FileIO {
    private var buffer: [UInt8]
    private var index: Int

    init(fileHandle: FileHandle = FileHandle.standardInput) {
        buffer = Array(fileHandle.readDataToEndOfFile()) + [UInt8(0)] // 인덱스 범위 넘어가는 것 방지
        index = 0
    }

    @inline(__always) private func read() -> UInt8 {
        defer { index += 1 }
        return buffer.withUnsafeBufferPointer { $0[index] }
    }

    @inline(__always) func readInt() -> Int {
        var sum = 0
        var now = read()
        var isPositive = true

        while now == 10 || now == 32 {
            now = read()
        }
        if now == 45 { isPositive.toggle(); now = read() }
        while now >= 48, now <= 57 {
            sum = sum * 10 + Int(now - 48)
            now = read()
        }

        return sum * (isPositive ? 1 : -1)
    }

    @inline(__always) func readInts(count: Int) -> [Int] {
        return (0 ..< count).map { _ in readInt() }
    }
}

let dataSet = FileIO()

// [Int] N (immutable): 입력 받을 수의 개수 (범위: 1 <= N <= 10,000,000)
let N: Int = dataSet.readInt()

// [Array<Int>] arrayOfCount (mutable): 10,000개 숫자의 발견 수를 저장하는 배열 (크기: 10,000+1)
var arrayOfCount: Array<Int> = [Int](repeating: 0, count: 10000+1)
                 
// N번 입력 받는다.
for _ in 0..<N {
    let number: Int = dataSet.readInt()
    
    arrayOfCount[number] += 1
}
        
// [String] stringOfResult (mutable): 시간초과를 방지하고자 한 번에 문자를 출력하기 위한 변수
var stringOfResult: String = ""
for (index, value) in arrayOfCount.enumerated() {
    stringOfResult += String(repeating: "\(index)\n", count: value)
}

print(stringOfResult)