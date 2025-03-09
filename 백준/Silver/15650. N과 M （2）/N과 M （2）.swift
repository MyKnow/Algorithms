// [func(inout Array<Array<Int>>), Array<Int>, Int, Int, Int)] printSequence
// : 주어진 조건에 맞는 수열을 배열에 저장하는 함수
// [inout Array<Array<Int>>] results: 조건에 맞는 수열을 저장하는 배열
// [inout Array<Int>] stack: 현재 DFS로 탐색 중인 수를 저장하는 배열
// [Int] N: 자연수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
// [Int] M: 수열의 길이 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
// [Int] start: DFS를 시작할 시작 index
func printSequence(
    _ results: inout [[Int]], 
    _ stack: inout [Int], 
    _ N: Int, 
    _ M: Int, 
    _ start: Int
) {
    // 1. 만약 스택의 길이가 M과 같다면 배열에 저장한다.
    if (stack.count == M) {
        results.append(stack)
        return
    }
    // 2. start부터 N까지 DFS를 진행한다.
    // 2-1. start가 N보다 작을 때만 실행한다.
    guard start <= N else { return }
    for index in start...N {
        // 3. 현재 index를 스택에 넣는다.
        stack.append(index)
        // 4. 현재 index 이후의 수로만 재귀적으로 호출한다.
        printSequence(&results, &stack, N, M, index+1)
        // 5. 스택에서 현재 index를 제거한다.
        stack.removeLast()
    }
}

if let input: String = readLine() {
    let arrayOfInput: [Int] = input.split(separator: " ").compactMap {
        Int($0)
    }
    // [Int] N (immutable): 자연수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
    // [Int] M (immutable): 수열의 길이 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
    let (N, M): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])
    
    // [Array<Array<Int>>] results (mutable): 조건에 맞는 수열을 저장하는 집합
    var results = [[Int]]()

    // [Array<Int>] stack (mutable): 수열을 저장하기 위한 스택
    var stack = [Int]()
    
    // DFS로 탐색하여 조건에 맞는 수열을 리스트에 저장한다.
    printSequence(&results, &stack, N, M, 1)
    
    // 배열에 저장된 값을 정렬하여 출력한다.
    for seq in results {
        print(seq.map { String($0) }.joined(separator: " "))
    }
}