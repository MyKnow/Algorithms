// [Int] N (immutable): N번째 영화의 제목에 들어 갈 수 (범위(자연수): <= 10,000)
let N = Int(readLine() ?? "1")

// [Int] nowNumber (mutable): 현재까지 찾은 조건에 부합한 수 (조건: 6이 3번 연속 들어간 수)
var nowNumber: Int = 666

// [Int] count (mutable): 찾은 조건에 부합한 수의 개수
var count: Int = 0

while (true) {
    // [Array<Int>] arrayOfNumber (immutable): nowNumber를 리스트로 쪼갠 것
    let arrayOfNumber: Array<Int> = Array(String(nowNumber).compactMap { Int(String($0)) })
    
    // [Int] countOfSix (mutable): 리스트 속 연속된 6의 개수
    var countOfSix: Int = 0
    for index in 0..<arrayOfNumber.count {
        if (arrayOfNumber[index] == 6) {
            countOfSix += 1
        }
        else {
            countOfSix = 0
        }
            
        if (countOfSix == 3) {
            count+=1
            break
        }
    }
    
    // N번째에 해당하는 수를 찾았다면 출력 및 종료
    if (count == N) {
        print(nowNumber)
        break
    }
    // 아니라면 nowNumber를 1 증가시킴
    nowNumber += 1
}