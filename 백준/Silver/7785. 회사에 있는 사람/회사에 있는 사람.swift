// [Int] n (immutable): 회사 로그에 기록된 출입 기록의 수 (범위(자연수): 2 <= n <= 1,000,000)
let n: Int = Int(readLine() ?? "2") ?? 2
 
// [Set<String>] setOfNames (mutable): 회사에 있는 모든 사람을 저장하는 집합 (크기: <= n)
var setOfNames: Set<String> = Set<String>()

// N회 반복
for _ in 0..<n {
    // [String] arrayOfInput (immutable): 각 로그에 적힌 사람의 이름[0]과 출입 여부[1]
    let arrayOfInput: Array<String> = (readLine() ?? "a enter").split(separator: " ").map { String($0) }
    
    // 출입로그 기록에 오류가 없다고 가정.
    // 로그에 enter라고 써 있으면 집합에 이름을 추가함.
    if (arrayOfInput[1] == "enter") {
        setOfNames.insert(arrayOfInput[0])
    }
    // 로그에 leave라고 써 있으면 집합에서 이름을 찾아 제거함.
    else {
        setOfNames.remove(arrayOfInput[0])
    }
}

// 완성된 로그를 리스트로 변환하고, 내림차순 정렬하여 출력
print(setOfNames.sorted(by: >).joined(separator: "\n"))