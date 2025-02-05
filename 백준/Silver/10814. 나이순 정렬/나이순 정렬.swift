// [Int] N (immutable): 입력 받을 회원 정보의 개수 (범위(정수): 1 ≤ N ≤ 100,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// [Array<Tuple(index: Int, age: Int, name: String)>] arrayOfPeople (mutable): 입력 받은 회원를 저장하는 배열 (길이: N)
var arrayOfPeople: Array<(index: Int, age: Int, name: String)> = Array<(index: Int, age: Int, name: String)>()

for index in 0..<N {
    let arrayOfInput: Array<String> = (readLine() ?? "21 Junkyu").split(separator: " ").map { String($0) }
    arrayOfPeople.append( ( index: index, age: Int(arrayOfInput[0]) ?? 0, name: arrayOfInput[1]) )
}

// 배열을 나이, 인덱스 순으로 오름차순 정렬한다.
arrayOfPeople.sort(by: { $0.age == $1.age ? $0.index < $1.index : $0.age < $1.age } )

// 출력
for (_, age, name) in arrayOfPeople {
    print("\(age) \(name)")
}