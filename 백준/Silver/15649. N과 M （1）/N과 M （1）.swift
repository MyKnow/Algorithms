// [func(inout Array<Bool>, inout Array<Int>, Int, Int)] printSequence
// : 충족되는 조건의 수열을 출력하는 함수
// [inout Array<Bool>] isVisited: 이미 탐색한 숫자인지 확인하는 리스트 (길이: N)
// [inout Array<Int>] stack: sequence에서 DFS로 탐색 중인 값을 저장하는 스택
// [Int] N: 자연수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
// [Int] M: 수열의 길이 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
func printSequence (
    _ isVisited: inout Array<Bool>, 
    _ stack: inout Array<Int>, 
    _ N: Int, 
    _ M: Int 
) {
    // 1. 스택의 길이가 수열 생성 조건이라면 출력함.
    if (stack.count == M) {
        print(stack.map { String($0) }
              .joined(separator: " "))
        
        return
    }

    // 2. 1부터 N까지 순회함.
    for index in 1...N {
        // 3. 만약 이미 방문한 적 있는 수라면 Continue함.
        if (isVisited[index]) {
            continue
        }
        // 4. 방문한 적 없는 수라면 스택에 삽입함.
        stack.append(index)
        // 5. 방문했으므로 isVisited를 true로 변경.
        isVisited[index] = true
        // 6. 함수를 재귀하여 수열을 완성시킴.
        printSequence(&isVisited, &stack, N, M)
        // 7. 사용한 수를 스택에서 제거하여 다음 수를 넣을 준비를 함.
        stack.removeLast()
        // 8. isVisited를 다시 false로 변경하여 다음 조건문을 대비함.
        isVisited[index] = false
    }
}

if let input: String = readLine() {
    // [Int] N (immutable): 자연수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
    // [Int] M (immutable): 수열의 길이 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
    let arrayOfInput: [Int] = input.split(separator: " ").compactMap { Int($0) }
    let (N, M): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])
    
    // [Array<Bool>] isVisited (mutable): Index가 이미 탐색한 숫자인지 확인하는 리스트 (길이: N+1)
    var isVisited = [Bool](repeating: false, count: N+1)

    // [Array<Int>] stack (mutable): sequence에서 DFS로 탐색 중인 값을 저장하는 스택
    var stack = [Int]()

    // 초기값을 바탕으로 함수를 실행시킴.
    printSequence(&isVisited, &stack, N, M)
}