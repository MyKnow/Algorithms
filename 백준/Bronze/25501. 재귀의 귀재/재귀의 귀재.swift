// [func<[String], Int, Int, Int> -> (Int, Int)] isPalindrome
// 해당 배열이 팰린드롬이면 (1, 호출횟수), 아니면 (0, 호출횟수)을 반환하는 함수.
func isPalindrome(str: [String], leftIndex: Int, rightIndex: Int, count: Int) -> (Int, Int) {
    // 1. 탐색이 종료되면 1을 반환한다.
    if (leftIndex >= rightIndex) {
        return (1, count)
    }
    // 2. 배열의 좌우가 서로 다르면 0을 반환한다.
    else if(str[leftIndex] != str[rightIndex]) {
        return (0, count)
    }
    // 3. 배열의 좌우가 같으면 다음 인덱스를 탐색한다.
    else {
        return isPalindrome(str: str, leftIndex: leftIndex+1, rightIndex: rightIndex-1, count: count+1)
    }
}

// [Int] T (immutable): 테스트 케이스의 개수 (범위(자연수): 1 <= T <= 1,000)
if let input = readLine(), let T = Int(input) {
    // [Array<String>] result (mutable)
    // 각 테스트 케이스에 해당하는 문자열을 저장한 배열 (길이: T)
    var result = [String]()
    
    for _ in 0..<T {
        if let S = readLine() {
            // [Array<String>] arrayOfS (mutable): 문자열 S를 배열로 변환
            var arrayOfS = [String]()
            
            for char in S {
                arrayOfS.append( String(char) )
            }
            // [(Int, Int)] torf, count
            // torf: 주어진 문자열 S가 팰린드롬이면 1, 아니면 0
            // count: isPalindrome 함수가 호출된 횟수
            let (torf, count) = isPalindrome(str: arrayOfS, leftIndex: 0, rightIndex: S.count-1, count: 1)

            result.append("\(torf) \(count)")
        }
    }

    print(result.joined(separator: "\n"))
}