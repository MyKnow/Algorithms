// [func(String) -> Bool] isVPS: 문자열을 입력 받으면, VPS인지 판단하여 bool을 반환한다.
func isVPS (_ s: String) -> Bool {
    // [Array<String>] arrayOfString (immutable): 문자열을 배열로 변환함.
    let arrayOfString: Array<String> = Array(s).map { String($0)}
    
    // [Array<String>] stack (mutable): 문자열을 저장할 배열
    var stack: Array<String> = [String]()
    
    for c in arrayOfString {
        // 1. 여는 괄호를 만나면 스택에 추가한다.
        if (c == "(" || c == "[") {
            stack.append(c)
        }
        // 2. 닫는 소괄호를 만나면, 조건을 검사한다.
        else if (c == ")") {
            // 2-1. 만약 스택이 비어있거나, 스택의 마지막이 여는 소괄호가 아니면 VPS가 아니다.
            if let last = stack.last {
                if last != "(" {
                    return false
                }
            } else {
                return false
            }
            // 2-2. 스택의 마지막이 여는 소괄호라면 제거한다.
            stack.popLast()
        }
        // 3. 닫는 대괄호를 만나면, 조건을 검사한다.
        else if (c == "]"){
            // 3-1. 만약 스택이 비어있거나, 스택의 마지막이 여는 대괄호가 아니면 VPS가 아니다.
            if let last = stack.last {
                if last != "[" {
                    return false
                }
            } else {
                return false
            }
            // 3-2. 스택의 마지막이 여는 대괄호라면 제거한다.
            stack.popLast()
        }
        else if (c == ".") {
            // 4-1. 스택의 길이를 확인하고, 비어있지 않다면 VPS가 아니다.
            if (stack.count != 0) {
                return false
            }
            else {
                return true
            }
        }
    }
    
    return true
}

while(true) {
    if let string = readLine() {
        if (string == ".") {
            break
        }
        else {
            print(isVPS(string) ? "yes" : "no")
        }
    }
}
    