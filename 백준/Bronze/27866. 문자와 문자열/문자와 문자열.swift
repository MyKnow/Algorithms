// S: String (immutable) - 사용자로부터 입력 받은 문자열
let S: String = readLine() ?? "a"

// i: Int (immutable) - 사용자로부터 입력 받은, 출력할 문자의 index+1
let i: Int = Int(readLine() ?? "1") ?? 1

// i-1번째 문자를 출력한다.
print(S[S.index(S.startIndex, offsetBy: i-1)])