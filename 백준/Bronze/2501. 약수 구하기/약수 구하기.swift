//[(Int, Int)] N, K (immutable): 약수 관계를 파악할 두 자연수 (범위: 1 <= K <= N <= 10,000)
let arrayOfInput: Array<Int> = (readLine() ?? "1 1").split(separator: " ").map {Int($0) ?? 1}
let N: Int = arrayOfInput[0]
let K: Int = arrayOfInput[1]

//[Array<Int>] factorsArray (mutable): N의 약수를 저장하는 배열
var factorsArray: Array<Int> = [Int]()

for number in 1...N {
    // number가 N의 약수인 경우 리스트에 추가한다.
    if (N % number == 0) {
        factorsArray.append(number)
    }
}

// factorsArray의 길이가 K보다 작다면 0을 출력한다.
print((factorsArray.count < K) ? 0 : factorsArray[K-1])