#include <string>
#include <vector>
#include <iostream>
#include <tuple>

using namespace std;

// # 문제 요약:
// - 가로 길이가 w인 창고에 지그재그로 n개의 상자를 쌓고, num번은 상자를 꺼내야 할 때,
// 꺼내야 하는 상자의 총 개수를 return하라
//
// # 입력:
// - n -> int: 상자 갯수
//      - 범위: 2 <= n <= 100
//
// - w -> int: 창고의 가로 길이
//      - 범위: 1 <= w <= 10
//
// - num -> int: 꺼내야 하는 상자 번호
//      - 범위: 1 <= num <= n
//
// # 출력:
// - result -> int: num번 상자를 꺼내기 위해, 꺼낸 총 상자 수
//      - 주의: num번 상자도 갯수에 포함해야 함.
//
// # 고찰:
// - 상자를 쌓는 건 어렵지 않게 w-1칸 전진, 상단으로 이동, 바뀐 방향으로 w-1칸 전진, ..., 으로 구현하면 될 것 같다.
//      - 시간복잡도: O(N)
// - 상자를 꺼내는 것은 해당 상자보다 높이 있는 상자를 꺼내면 되므로, num에 해당하는 상자의 위치를 미리 기록해놓고, 추
// 후 해당 index보다 높은(또는 낮은) 행에 있는 상자의 갯수를 count하면 될 것 같다.
//
// # 설계:
// - index 관리를 쉽게 하기 위해서, 예시 이미지를 상하 반전하고, 중력이 반전되어있는 것처럼 아래에서부터 꺼내는 식으로 
// 푸는 게 나을 것 같다.

int solution(int n, int w, int num) {
    int limit_y = n/w+1;
    
    // warehouse: 가로 길이 w, 세로 길이 (n/w)+1의 2중 int vector
    vector<vector<int>> warehouse(limit_y, vector<int>(w, 0));
    
    // directions: 우, 좌 방향 벡터
    vector<pair<int, int>> directions = {{1, 0}, {-1, 0}};
    
    // next: 다음 방향으로 전환하는 원형 인덱싱 람다 함수
    int v_idx = 0;
    auto next = [&](int step = 1) {
        v_idx = (v_idx + step + directions.size()) % directions.size();
        return directions[v_idx];
    };
    
    // move: 다음 방향으로 이동하는 람다함수
    auto move = [&](int cx, int cy) {
        return make_pair(cx+directions[v_idx].first, cy+directions[v_idx].second);
    };
    
    // crt_pos: 현재 위치
    pair<int, int> crt_pos = {0, 0};
    
    // num_pos: num번 상자의 위치(초기값: {0, 0})
    pair<int, int> num_pos = {0, 0};
    
    for (int i = 1; i <= n; i++) {
        // cx, cy: 현재 위치
        int cx, cy; tie(cx, cy) = crt_pos;
        
        // i값으로 현재 위치에서의 상자 값 업데이트
        warehouse[cy][cx] = i;
        
        // num번 상자의 위치는 기록해놓는다.
        if (i == num) { num_pos = crt_pos; }
        
        // sx, sy: directions에 의해 이동된 위치
        int sx, sy; tie(sx, sy) = move(cx, cy);
        
        // 만약 다음 이동 시 범위를 벗어나게 된다면, 이전 이동을 취소하고, 한 칸 밑으로 이동한 후 방향을 돌린다.
        if (!((0 <= sx && sx < w) && (0 <= sy && sy < limit_y))) {
            crt_pos = make_pair(cx, ++cy);
            next(); 
        }
        // 그렇지 않다면 정상적으로 진행한다.
        else { crt_pos = make_pair(sx, sy); }
    }
    
    // num_pos의 y값을 증가시키며, 0(초기화되지 않은 상자)값이거나 y 범위를 벗어나게 될 때까지의 깊이를 측정한다.
    int answer = 0;
    cout << limit_y << endl;
    for (int y = num_pos.second; (warehouse[y][num_pos.first] != 0) && (y < limit_y); y++) { 
        answer++; 
        cout << answer << endl;
    }
    return answer;
}