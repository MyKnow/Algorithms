while(true) {
    // [Int] n (immutable): 완전수 여부를 파악할 자연수 (범위: 2 < n < 100,000)
    let n: Int = Int(readLine() ?? "3") ?? 3
    
    // -1이 입력되면 반복문을 종료한다.
    if (n == -1) {
        break
    }

    // [Array<Int>] factorsArray (mutable): n을 제외한 n의 약수를 저장하는 리스트
    var factorsArray: Array<Int> = [Int]()

    // n을 제외해야 하기 때문에 range의 범위를 1부터 n-1로 지정한다.
    for number in 1..<n {
        // number가 N의 약수인 경우 리스트에 추가한다.
        if (n % number == 0) {
            factorsArray.append(number)
        }
    }
            
    // [Int] sumOfFactors (immutable): 약수들의 합을 저장하는 변수
    let sumOfFactors: Int = factorsArray.reduce(0, +)
    
    // 만약 완전수라면 지정된 출력에 맞춰 출력한다.
    if (n == sumOfFactors) {
        print("\(n) = \(factorsArray.map { String($0) }.joined(separator: " + "))")
    }
    else {
        print("\(n) is NOT perfect.")
    }
}