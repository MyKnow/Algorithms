// [Int] N (immutable): 명령의 수 (범위(자연수): 1 ≤ N ≤ 1,000,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Array<Int>] stack (mutable): 정수를 저장할 스택
var stack: Array<Int> = [Int]()

for _ in 0..<N {
    if let order = readLine() {
        // 명령어가 1글자 초과인 경우, "1 X" 형태임.
        // 1. X를 스택에 넣기.
        if (order.count > 1) {
            stack.append( (order.split(separator: " ").compactMap { Int($0) })[1] )
        }
        // 2. 스택에 정수가 존재할 경우 빼고 출력한다.
        // 없다면 -1을 대신 출력한다.
        else if ((Int(order) ?? 0) == 2) {
            if let lastValue = stack.last {
                print(lastValue)
                stack.removeLast()
            } else {
                print(-1)
            }
        }
        // 3. 스택에 들어있는 정수의 개수를 출력한다.
        else if ((Int(order) ?? 0) == 3) {
            print(stack.count)
        }
        // 4. 스택이 비어있으면 1, 아니면 0을 출력한다.
        else if ((Int(order) ?? 0) == 4) {
            if (stack.count == 0) {
                print(1)
            } else {
                print(0)
            }
        }
        // 5. 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 출력한다.
        else if ((Int(order) ?? 0) == 5) {
            if let lastValue = stack.last {
                print(lastValue)
            } else {
                print(-1)
            }
        }
    }
}