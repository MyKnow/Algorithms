// [Int] N, M (immutable)
// N: 도감에 수록되어 있는 포켓몬의 개수
// M: 다솜이가 맞춰야 하는 문제의 개수
// 범위(자연수): 1 <= N, M <= 100,000
let arrayOfInput: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
let (N, M): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

// [Dictionary<String, String)] dictOfPocketmon (mutable): 입력 받은 포켓몬의 (이름:번호)쌍을 저장하는 사전 (길이: N)
var dictOfPocketmon: Dictionary<String, String> = Dictionary<String, String>()

// 포켓몬의 개수만큼 사전을 초기화한다.
for index in 1...N {
    let input: String = readLine() ?? "error"
    
    dictOfPocketmon[input] = String(index)
    dictOfPocketmon[String(index)] = input
}

// 문제의 수만큼 반복한다.
for _ in 0..<M {
    let question: String = readLine() ?? "0"
    
    // 문제가 숫자라면 숫자를 키값으로 활용하여 이름을 출력한다.
    if let number = Int(question) {
        print(dictOfPocketmon[String(number)] ?? "error")
    }
    // 문제가 이름이라면 이름을 키값으로 활용하여 번호를 출력한다.
    else {
        print(dictOfPocketmon[question] ?? "0")
    }
}