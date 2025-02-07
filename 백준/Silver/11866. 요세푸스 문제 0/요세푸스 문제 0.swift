struct Deque {
    var nums: [Int] = [Int]()
    var start: Int = 0
    var end: Int = 0
    
    var isEmpty: Bool {
        return start == end
    }
    
    var size: Int {
        return end - start
    }
    
    var first: Int {
        if (isEmpty) {
            return -1
        }
        return nums[start]
    }
    
    var last: Int {
        if (isEmpty) {
            return -1
        }
        return nums[end-1]
    }
    
    mutating func append(_ num: Int) {
        nums.append(num)
        end += 1
    }
    
    mutating func pop() -> Int {
        if (isEmpty) {
            return -1
        }
        let num: Int = first
        start += 1
        return num
    }
}

// [Int] N, K (immutable)
// N: 원을 이룬 사람들의 수
// K: 사람을 제거할 간격
// 범위(자연수): 1 <= K <= N <= 1,000
let arrayOfInput: [Int] = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
let (N, K): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

// [Deque] originalDQ (mutable): 순서대로 사람이 서 있는 deque
var originalDQ: Deque = Deque()
for number in 1...N {
    originalDQ.append(number)
}
    
// [Array<Int>] result (mutable): 제거된 사람을 저장하는 배열
var result: Array<Int> = [Int]()

while(!originalDQ.isEmpty) {
    for _ in 0..<K-1 {
        originalDQ.append(originalDQ.pop())
    }
    result.append(originalDQ.pop())
}
    
// [String] resultForOutput (immutable): 출력 포맷에 맞게 수정된 result
let resultForOutput: String = result.map { String($0) }.joined(separator: ", ")

// 출력
print("<\(resultForOutput)>")