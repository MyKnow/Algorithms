import Foundation

// 빠른 입출력을 위한 클래스 선언
final class FileIO {
    private var buffer:[UInt8]
    private var index: Int
    
    init(fileHandle: FileHandle = FileHandle.standardInput) {
        buffer = Array(fileHandle.readDataToEndOfFile())+[UInt8(0)]
        index = 0
    }
    
    @inline(__always) private func read() -> UInt8 {
        defer { index += 1 }
        return buffer[index]
    }
    
    @inline(__always) func readInt() -> Int {
        var sum = 0
        var now = read()
        var isPositive = true
        
        while now == 10 || now == 32 { now = read() }
        if now == 45 { isPositive.toggle(); now = read() }
        while now >= 48, now <= 57 {
            sum = sum * 10 + Int(now-48)
            now = read()
        }
        return isPositive ? sum : -sum
    }
}

// 두 개의 스택을 맞붙힌 모양의 Deque
struct Deque {
    // [Int] leftIndex (mutable): Deque의 left 위치를 가리키는 변수
    private var leftIndex: Int
    
    // [Int] rightIndex (mutable): Deque의 right 위치를 가리키는 변수
    private var rightIndex: Int
    
    // [Int] maxCount (immutable): Deque의 전체 크기를 가리키는 변수
    private let maxCount: Int
    
    // [Array<String>] values (mutable): Deque의 값을 저장하는 변수
    private var values: Array<String>
    
    init(_ length: Int) {
        leftIndex = length / 2
        rightIndex = length / 2
        values = [String](repeating: "-1", count: length)
        maxCount = length
    }
    
    // [String] count (computed): Deque의 길이를 계산하는 변수
    var count: String {
        return String(rightIndex - leftIndex)
    }
    
    // [String] isEmpty (computed): Deque가 비어있는 지 확인하는 변수
    var isEmpty: String {
        return leftIndex == rightIndex ? "1" : "0"
    }
    
    // [String] left (computed): Deque의 left에 위치한 값을 출력하는 변수
    var left: String {
        return isEmpty == "1" ? "-1" : values[leftIndex]
    }
    
    // [String] right (computed): Deque의 right에 위치한 값을 출력하는 변수
    var right: String {
        return isEmpty == "1" ? "-1" : values[rightIndex-1]
    }
    
    // [func(String)] appendLeft: Deque의 left에 값을 추가하는 함수
    mutating func appendLeft(_ value: String) {
        if (leftIndex > 0) {
            leftIndex -= 1
            values[leftIndex] = value
        }
    }
    
    // [func(String)] appendRight: Deque의 right에 값을 추가하는 함수
    mutating func appendRight(_ value: String) {
        if (rightIndex < maxCount - 1) {
            rightIndex += 1
            values[rightIndex-1] = value
        }
    }
    
    // [func() -> String] popLeft: Deque의 left의 값을 제거하여 출력하는 함수
    mutating func popLeft() -> String {
        if (isEmpty == "1") {
            return "-1"
        } else {
            let value: String = values[leftIndex]
            leftIndex += 1
            return value
        }
    }
    
    // [func() -> String] popRight: Deque의 right의 값을 제거하여 출력하는 함수
    mutating func popRight() -> String {
        if (isEmpty == "1") {
            return "-1"
        } else {
            rightIndex -= 1
            return values[rightIndex]
        }
    }
}

// [FileIO] file (immutable): 빠른 입출력을 위한 클래스
let file: FileIO = FileIO()

// [Int] N (immutable): 명령어의 수 (범위(자연수): 1 ≤ N ≤ 1,000,000)
let N: Int = file.readInt()

// [Deque] dq (mutable): Int를 저장하는 deque (길이: <= 2N)
var dq: Deque = Deque(N*2)

// [Array<String>] result (mutable): 각 명령어의 수행 결과를 저장하는 배열(길이: <= N)
var result: Array<String> = [String]()

for _ in 0..<N {
    // [Int] command (immutable): 현재 명령어
    let command: Int = file.readInt()
    
    // 1. appendleft()
    if (command == 1){
        // [String] value (immutable): Deque에 저장할 값
        let value: String = String(file.readInt())
        
        dq.appendLeft(value)
    } 
    // 2. appendRight()
    else if (command == 2) {
        // [String] value (immutable): Deque에 저장할 값
        let value: String = String(file.readInt())
        
        dq.appendRight(value)
    }
    // 3. popleft()
    else if (command == 3) {
        result.append(dq.popLeft())
    }
    // 4. pop()
    else if (command == 4) {
        result.append(dq.popRight())
    }
    // 5. count
    else if (command == 5) {
        result.append(dq.count)
    }
    // 6. isEmpty
    else if (command == 6) {
        result.append(dq.isEmpty)
    }
    // 7. left
    else if (command == 7) {
        result.append(dq.left)
    }
    // 8. right
    else if (command == 8) {
        result.append(dq.right)
    }
}

print(result.joined(separator: "\n"))