// [func(inout Array<Int>, Int, Int)] printSequence
// : 주어진 조건에 맞는 수열을 results에 저장하는 함수
// [inout Array<Int>] stack: 현재 DFS로 탐색 중인 수를 저장하는 배열
// [Int] N: 자연수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
// [Int] M: 수열의 길이 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
func printSequence(
    _ stack: inout [Int], 
    _ N: Int, 
    _ M: Int
) {
    // 1. 만약 스택의 길이가 M과 같다면 리스트에 저장한다.
    if (stack.count == M) {
        print(stack.map {String($0)}.joined(separator: " "))
        return
    }
    // 2. 1부터 N까지 DFS를 진행한다.
    for index in 1...N {
        // 3. 스택의 최상단이 존재할 때, 현재 index가 최상단보다 작다면 넘긴다.
        if let top: Int = stack.last {
            if index < top {
                continue
            }
        }
        // 4. 현재 index를 스택에 넣는다.
        stack.append(index)
        // 5. 현재 index를 포함하여 재귀적으로 호출한다.
        printSequence(&stack, N, M)
        // 6. 스택에서 현재 index를 제거한다.
        stack.removeLast()
    }
}
    
if let input = readLine() {
    let arrayOfInput: [Int] = input.split(separator: " ").compactMap { Int($0) }
    // [int] N: 자연수의 범위 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
    // [int] M: 수열의 길이 (범위(자연수): 1 ≤ M ≤ N ≤ 8)
    let (N, M): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

    // [Array<Int>] stack (mutable): 현재 DFS로 탐색 중인 수를 저장하는 배열
    var stack = [Int]()
    
    // DFS로 탐색하여 조건에 맞는 수열을 출력한다.
    printSequence(&stack, N, M)
}