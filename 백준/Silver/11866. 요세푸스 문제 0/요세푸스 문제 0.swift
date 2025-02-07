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
        let num: Int = nums[start]
        start += 1
        return num
    }
    
    mutating func rotate(_ num: Int) {
        // size가 0일 경우 회전하지 않음
        guard size > 0 else { return }
        
        // 양수로만 값이 들어오기 때문에, left rotation만 구현함.
        for _ in 0..<num-1 {
            self.append(self.pop())
        }
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
    // 1. deque를 왼쪽으로 K칸 회전시킨다.
    originalDQ.rotate(K)
    
    // 2. 회전된 deque의 첫번째 요소를 pop하여 result에 넣는다.
    result.append(originalDQ.pop())
}
    
// [String] resultForOutput (immutable): 출력 포맷에 맞게 수정된 result
let resultForOutput: String = result.map { String($0) }.joined(separator: ", ")

// 출력
print("<\(resultForOutput)>")