struct Queue {
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
        if isEmpty {
            return -1
        }
        return nums[start]
    }
    
    var last: Int {
        if isEmpty {
            return -1
        }
        return nums[end-1]
    }
    
    mutating func pop() -> Int {
        if isEmpty {
            return -1
        }
        
        let num: Int = nums[start]
        
        start += 1
        
        return num
    }
    
    mutating func append(_ num: Int) {
        nums.append(num)
        end += 1
    }
}

// [Int] N (immutable): 제일 아래에 있는 카드 번호 (범위(자연수): 1 <= N <= 500,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Queue] cardStack (mutable): 1부터 N까지 오름차순으로 정리된 카드덱 (길이: N)
var cardStack: Queue = Queue()

for number in 1...N {
    cardStack.append(number)
}

while (cardStack.size > 2) {
    // 1. 카드 최상단을 버린다.
    cardStack.pop()
    
    // 2. 1번을 수행한 덱에서, 최상단에 있는 카드를 제일 아래로 옮긴다.
    cardStack.append( cardStack.pop() )
}
    
// 만약 카드덱 길이가 1이라면, 첫번째 요소를, 2라면 마지막 요소를 출력한다.
print(cardStack.size == 1 ? cardStack.first : cardStack.last)