let testCase: Int = Int(readLine() ?? "1") ?? 1

var array = [[Int]](repeating: [Int](repeating:0, count: 6), count: testCase)

for i in 0..<array.count {
    array[i] = (readLine() ?? "1 1 1 1 1 1").split(separator: " ").map{ Int($0) ?? 0 }
}

for j in 0..<array.count {
    let distance = (array[j][0] - array[j][3]) * (array[j][0] - array[j][3]) + (array[j][1] - array[j][4]) * (array[j][1] - array[j][4])
    let radiusAdd = (array[j][2] + array[j][5]) * (array[j][2] + array[j][5])
    let radiusDif = (array[j][2] - array[j][5]) * (array[j][2] - array[j][5])
    
    // 첫번째 케이스 : 완전히 겹칠 때
    if distance == 0 && radiusDif == 0 {
        print(-1)
    }
    // 두번째 케이스 : 두 점에서 만날 때
    else if radiusDif < distance && distance < radiusAdd {
        print(2)
    }
    // 세번째 케이스 : 한 점에서 만날 때
    else if distance == radiusAdd || distance == radiusDif {
        print(1)
    }
    // 마지막 케이스 : 안 만날 때
    else {
        print(0)
    }
}