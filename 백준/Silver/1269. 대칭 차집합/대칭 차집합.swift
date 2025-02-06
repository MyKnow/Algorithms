// [Int] N, M (immutable): 두 집합 A, B의 원소의 개수 (범위: < 200,000)
let arrayOfInput: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
let (N, M): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

// [Set<Int>] A (immutable): 입력 받은 숫자를 저장하는 집합 (값: < 100,000,000)
let A: Set<Int> = Set<Int>( (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) } )

// [Set<Int>] B (immutable):: 입력 받은 숫자를 저장하는 집합 (값: < 100,000,000)
let B: Set<Int> = Set<Int>( (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) } )

// 답 출력
print( A.subtracting(B).count + B.subtracting(A).count)