// [Int] N (immutable): 승환이 앞에 서 있는 학생들의 수 (범위(자연수): (1 ≤ N ≤ 1,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Array<Int>] nowLine (mutable): 현재 승환이 앞에 서 있는 학생들의 줄을 의미하는 스택
var nowLine: Array<Int> = (readLine() ?? "1").split(separator: " ").compactMap { Int($0) }.reversed()

// [Array<Int>] subLine (mutable): 한 명씩만 설 수 있는 예비 대기열 스택
var subLine: Array<Int> = [Int]()

// [Int] enterNumber (mutable): 현재 입장 가능한 번호 (초기값: 1)
var enterNumber: Int = 1

while(true) {
    // 1. 스택이 모두 비어 있는 지 확인한다.
    if (nowLine.isEmpty && subLine.isEmpty) {
        print("Nice")
        break
    }
    // 2. 현재 대기열에서 바로 입장할 수 있다면 스택에서 삭제하고, enterNumber를 1 증가시킨다.
    else if let last = nowLine.last, last == enterNumber {
        nowLine.removeLast()
        enterNumber += 1
    }
    // 3. 임시 대기열에서 바로 입장할 수 있다면 스택에서 삭제하고, enterNumber를 1 증가시킨다.
    else if let last = subLine.last, last == enterNumber {
        subLine.removeLast()
        enterNumber += 1
    }
    // 4. 현재 대기열에서 임시 대기열로 사람을 이동시킬 수 있는 지 확인한다.
    else if let lastOfNow = nowLine.last {
        // 4-1. 임시 대기열이 비어 있다면 무조건 옮길 수 있다.
        if (subLine.isEmpty) {
            if let moved = nowLine.popLast() {
                subLine.append(moved)
            }
        }
        // 4-2. 임시 대기열이 존재하나 lastOfNow보다 큰 수가 최상단이라면 옮길 수 있다.
        else if let lastOfSub = subLine.last, lastOfSub > lastOfNow {
            if let moved = nowLine.popLast() {
                subLine.append(moved)
            }
        }
        // 4-3. 옮길 수 없다면 아무런 행동도 취할 수 없다는 의미이므로 종료한다.
        else {
            print("Sad")
            break
        }
        
    }
    // 5. 아무런 행동도 할 수 없다면 간식을 받을 수 없는 상태다.
    else {
        print("Sad")
        break
    }
}