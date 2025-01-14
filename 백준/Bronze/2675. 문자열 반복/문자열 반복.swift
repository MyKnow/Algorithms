// [Int] T (immutable): 테스트 케이스의 개수 (1 <= T <= 1,000)
let T: Int = Int(readLine() ?? "1") ?? 1

// T회 반복함
for _ in 0..<T {
    let inputOfEachCase: Array<String> = (readLine() ?? "1 A").split(separator: " ").map(String.init)
    
    // [Int] R (immutable): 문자열에서 각 문자를 반복할 횟수 (1 <= R <= 8)
    let R: Int = Int(inputOfEachCase[0]) ?? 1
    // [String] S (immutable) : 새 문자열을 만들 때 쓸 원본 문자열 (길이 : 1 <= len < 20)
    let S: String = inputOfEachCase[1]
    
    // S의 글자들을 반복문으로 인덱싱함
    for char in S {
        // 분리된 글자인 char를 String으로 변환하고, R회 반복하여 출력함
        print(String(repeating: char, count: R), terminator: "")
    }
    
    // 모든 글자를 출력하면 개행함
    print("")
}