// [Int] N (immutable): 사람들이 만난 기록의 수 (범위(자연수): 1 <= N <= 1,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Set<String>] rainbow (mutable): 무지개 댄스를 추는 사람의 집합
// 초기값: ChongChong (처음부터 무지개 댄스를 추는 사람)
var rainbow: Set<String> = ["ChongChong"]


for _ in 0..<N {
    // [Array<String>] log (immutable): 만난 두 사람을 저장한 리스트 (길이: 2)
    let log: [String] = (readLine() ?? "a b")
        .split(separator: " ")
        .map(String.init)
    
    // 만약 log 속 사람 중에 한 명이라도 rainbow 집합에 포함되어 있다면
    // 두 사람을 모두 rainbow 집합에 추가함.
    for people in log {
        if (rainbow.contains(people)) {
            rainbow.formUnion(log)
            break
        }
    }
}

// 무지개 댄스를 추는 사람의 수를 출력
print(rainbow.count)