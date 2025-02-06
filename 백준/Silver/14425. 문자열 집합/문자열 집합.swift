// [Int] N, M (immutable): 집합 S에 포함되어 있는 문자열 개수와 검사 대상인 문자열 개수 (범위(자연수): 1 <= N, M <= 10,000)
let arrayOfInput: Array<Int> = (readLine() ?? "1 1").split(separator: " ").compactMap { Int($0) }
let (N, M): (Int, Int) = (arrayOfInput[0], arrayOfInput[1])

// [Set<String>] setOfWords (mutable): N개의 문자열을 저장할 집합 (크기: N)
var setOfWords: Set<String> = Set<String>()

for _ in 0..<N {
    setOfWords.insert( (readLine() ?? "a") )
}
    
// [Array<String>] arrayOfWords (mutable): M개의 문자열을 저장할 배열 (크기: M)
var arrayOfWords: Array<String> = [String]()
for _ in 0..<M {
    arrayOfWords.append( (readLine() ?? "a") )
}

// [Int] count (mutable): 집합 S에 포함된 단어의 개수를 저장하는 변수
var count: Int = 0

// setOfWords에 arrayOfWords의 단어가 포함되어 있으면 count를 1 증가시킨다.
for word in arrayOfWords {
    if (setOfWords.contains(word)) {
        count+=1
    }
}

// count 출력
print(count)