// [String] word (immutable) : 알파벳 소문자로만 이루어진 단어 (길이: 1 <= len <= 100)
let word: String = readLine() ?? "a"

// 팰린드롬이면 1, 아니면 0을 출력한다.
print((word == String(word.reversed()) ? 1 : 0))