// [Int] N, M (immutable)
// N: 듣도 못한 사람의 수 
// M: 보도 못한 사람의 수
// (범위(자연수): <= 20)
let arrayOfInput: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
let (N, M): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

// [Set<String>] setOfN (mutable): 듣도 못한 사람을 저장하는 집합 (길이: N)
var setOfN: Set<String> = Set<String>()

// [Set<String>] setOfM (mutable): 보도 못한 사람을 저장하는 집합 (길이: N)
var setOfM: Set<String> = Set<String>()

for _ in 0..<N {
    setOfN.insert( readLine() ?? "A" )
}
    
for _ in 0..<M {
    setOfM.insert( readLine() ?? "A" )
}
    
// [Set<String>] setOfIntersection (immutable): 듣도 보도 못한 사람을 저장하는 집합 (길이: <= N, M)
let setOfIntersection: Set<String> = setOfN.intersection(setOfM)

// 출력
print(setOfIntersection.count)
print(setOfIntersection.sorted().map { String($0) }.joined(separator: "\n"))