// [Int] N (immutable): 도착해야 하는 목표 방 번호 (범위: 1 <= N <= 1,000,000,000)
let N: Int = Int(readLine() ?? "1") ?? 1

// 1번 방을 2번~7번방이 감싸고, 이를 8번방~19번방이 감싸는 규칙적인 구조이므로, N번방의 궤도 번호를 알아내면 쉽게 풀 수 있다.
// 1번 방의 궤도 번호를 1, 2~7번방이 속한 궤도 번호를 2, ... 로 정의한다.
// 각 궤도를 구성하는 방의 개수는 다음과 같다.
// 1: 1
// 2: 6
// 3: 12 
// 4: 18
// 5: 24
// 6: 30
// ...
// 2번 궤도부터 필요한 방의 수가 6개씩 증가하는 것을 알 수 있다.

// [Int] requireRoomsOfNowOrbit (mutable): 현재 궤도를 구성하기 위해 필요한 방의 개수의 총합
var requireRoomsOfNowOrbit: Int = 0

// [Int] lastRoomOfNowOrbit (mutable): 현재 탐색 중인 궤도의 마지막 방 번호
var lastRoomOfNowOrbit: Int = 1

// [Int] nowOrbitIndex (mutable): 현재 탐색 중인 궤도 번호
var nowOrbitIndex: Int = 1

// 목표 방 번호가 속해있는 궤도를 벗어나기 전까지 반복함.
while(lastRoomOfNowOrbit < N) {
    // 궤도 구성에 필요한 방 개수를 6씩 더한다.
    requireRoomsOfNowOrbit+=6
    
    // lastRoomOfNowOrbit에 requireRoomsOfNowOrbit를 더하여 마지막 방 번호를 계산한다.
    lastRoomOfNowOrbit += requireRoomsOfNowOrbit
    
    // nowOrbitIndex를 1 증가시킨다.
    nowOrbitIndex+=1
}

// 현재 궤도 번호를 출력한다.
print(nowOrbitIndex)