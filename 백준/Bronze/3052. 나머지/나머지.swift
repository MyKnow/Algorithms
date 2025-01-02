// func getSolutionWithArray -> void - Array로 해답을 구하는 함수
func getSolutionWithArray() {
    // arrayOfRemainder: Array<Int> (mutable) - 음이 아닌 정수로 구성된 1000 이하의 자연수를 42로 나눈 나머지를 저장하는 배열
    var arrayOfRemainder: Array<Int> = []
    
    // 숫자를 입력 받아서 42를 나누고, 이를 배열에 추가하는 과정을 10번 반복
    for _ in 0..<10 {
        // remainder: Int (immutable) - 숫자를 입력 받고 42로 나눈 나머지 (0 <= remainder < 42)
        var remainder: Int = (Int(readLine() ?? "0") ?? 0) % 42
        
        // arrayOfRemainder에 해당 나머지가 없다면 추가
        if (arrayOfRemainder.firstIndex(of: remainder) == nil) {
            arrayOfRemainder.append(remainder)
        }
    }
    // 배열의 길이를 출력 (서로 다른 나머지의 개수)
    print(arrayOfRemainder.count)
}

// 리스트의 길이를 출력 (서로 다른 나머지의 개수)
getSolutionWithArray()