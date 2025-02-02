while(true) {
    // [Int] s1, s2, s3 (immutable): 삼각형의 세 변
    let inputOfArray: Array<Int> = (readLine() ?? "0 0 0 ").split(separator: " ").compactMap { Int($0) }
    let (s1, s2, s3): (Int, Int, Int) = (inputOfArray[0], inputOfArray[1], inputOfArray[2])

    // 종료 조건 (0, 0, 0 입력 시)
    if (s1 == 0 && s2 == 0 && s3 == 0) {
        break
    }
    
    // 삼각형 조건 (삼각형 부등식 체크)
    if (s1 + s2 <= s3 || s1 + s3 <= s2 || s2 + s3 <= s1) {
        print("Invalid")
    }
    else {
        // [Int] uniqueSides (immutable): 변의 개수에 따른 삼각형 판별을 위한 set 길이 변수
        let uniqueSides: Int = Set([s1, s2, s3]).count

        if (uniqueSides == 1) {
            print("Equilateral") // 정삼각형
        }
        else if (uniqueSides == 2) {
            print("Isosceles")  // 이등변 삼각형
        }
        else {
            print("Scalene") // 부등변 삼각형
        }
    }
}