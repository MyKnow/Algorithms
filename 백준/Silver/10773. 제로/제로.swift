// [Int] K (immutable): 입력받을 명령어의 개수 (범위(자연수): 1 ≤ K ≤ 100,000)
let K: Int = Int(readLine() ?? "1") ?? 1

// [Array<Int>] stack (mutable): 계산할 정수를 담아두는 배열 (값 범위: 0 <= number <= 1,000,000)
var stack: Array<Int> = [Int]()

for _ in 0..<K {
    let order = Int(readLine() ?? "1") ?? 1
    
    // 1. 명령어가 0인 경우, 스택 최상단에서 요소를 하나 제거한다.
    if (order == 0) {
        stack.removeLast()
    }
    // 2. 0을 제외한 정수인 경우, 스택 최상단에 해당 정수를 추가한다.
    else {
        stack.insert(order, at: stack.endIndex)
    }
}

// 스택에 있는 모든 정수를 더하여 출력한다.
print(stack.reduce(0, +))