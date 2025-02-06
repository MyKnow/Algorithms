// [Int] T (immutable): 테스트 데이터의 개수 
let T: Int = Int(readLine() ?? "1") ?? 1

for _ in 0..<T {
    // [Array<String>] arrayOfString (immutable): "("와 ")"로 구성된 문자열을 배열로 변환함.
    let arrayOfString: Array<String> = Array(readLine() ?? "(").map { String($0) }
    
    // [Array<String>] stack (mutable): "("와 ")"로 구성된 스택
    var stack: Array<String> = Array<String>()
    
    // [Bool] isVPS (mutable): 올바른 괄호 문자열인지 판단하는 변수
    var isVPS: Bool = true
    for p in arrayOfString {
        // 1. 여는 괄호를 만나면 스택에 넣는다.
        if (p == "(") {
            stack.append(p)
        }
        // 2. 닫는 괄호를 만나면 스택에서 뺀다.
        else {
            // 2-1. 만약, 스택이 비어있다면 올바른 문자열이 아니므로 바로 종료한다.
            if (stack.count == 0) {
                isVPS = false
                break
            }
            // 2-2. 스택에 괄호가 존재하면 제거한다.
            else {
                stack.popLast()
            }
        }
    }
    // stack이 비어있고, 여는 괄호가 올바르게 모두 제거된 상태일 때
    if (stack.count == 0 && isVPS) {
        print("YES")
    }
    else {
        print("NO")
    }
}