import Foundation

final class FileIO {
    private var buffer:[UInt8]
    private var index: Int

    init(fileHandle: FileHandle = FileHandle.standardInput) {
        
        buffer = Array(fileHandle.readDataToEndOfFile())+[UInt8(0)] // 인덱스 범위 넘어가는 것 방지
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

        while now == 10
            || now == 32 { now = read() } // 공백과 줄바꿈 무시
        if now == 45{ isPositive.toggle(); now = read() } // 음수 처리
        while now >= 48, now <= 57 {
            sum = sum * 10 + Int(now-48)
            now = read()
        }

        return sum * (isPositive ? 1:-1)
    }

    @inline(__always) func readString() -> Int {
        var str = 0
        var now = read()

        while now == 10
            || now == 32 { now = read() } // 공백과 줄바꿈 무시

        while now != 10
            && now != 32 && now != 0 {
                str += Int(now)
                now = read()
        }
        
        return str
    }
}

func stringToAscii(_ str: String) -> Int {
    str.map { $0.asciiValue! }.map { Int($0) }.reduce(0) {$0 + $1}
}

let FRONT = stringToAscii("front")
let EMPTY = stringToAscii("empty")
let BACK = stringToAscii("back")
let SIZE = stringToAscii("size")
let POP = stringToAscii("pop")

struct Queue {
    private var nums = [Int]()
    private var start = 0
    private var end = 0
    
    var isEmpty: Bool {
        start == end
    }
    
    var size: Int {
        end - start
    }
    
    mutating func pop() -> Int {
        if isEmpty {
            return -1
        }
        
        let num: Int = nums[start]
        
        start += 1
        
        return num
    }
    
    var front: Int {
        if isEmpty {
            return -1
        }
        return nums[start]
    }
    
    var back: Int {
        if isEmpty {
            return -1
        }
        return nums[end-1]
    }
    
    mutating func push(_ num: Int) {
        nums.append(num)
        end += 1
    }
}

let file = FileIO()

// [Int] N (immutable): 주어진 명령의 수 (범위: 1 ≤ N ≤ 2,000,000)
let N: Int = file.readInt()

// [Queue] queue (mutable): 정수를 저장하는 큐 구조체
var queue: Queue = Queue()

// [Array<Int>] result: (mutable): 출력할 결과를 저장하는 배열
var result: [Int] = [Int]()

for _ in 0..<N {
    let order: Int = file.readString()
        
    // 1. pop: queue의 가장 앞에 있는 정수를 빼서 출력하는 연산
    if order == POP {
        result.append(queue.pop())
    }
    // 2. size: queue에 들어있는 정수 개수 출력
    else if order == SIZE {
        result.append(queue.size)
    }
    // 3. empty: 큐가 비어있으면 1, 아니면 0 출력
    else if order == EMPTY {
        result.append( (queue.isEmpty ? 1 : 0) )
    }
    // 4. front: 큐의 가장 앞 정수를 출력, 없으면 -1
    else if order == FRONT {
        result.append( queue.front )
    }
    // 5. back: 큐의 가장 뒤 정수를 출력, 없으면 -1
    else if order == BACK {
        result.append( queue.back )
    }
    // 6. push X: 정수 X를 queue에 넣는 연산
    else {
        let X = file.readInt()
        queue.push(X)
    }
}

// 최종 결과 출력
print(result.map { String($0) }.joined(separator: "\n"))