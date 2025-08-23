#include <string>
#include <vector>
#include <utility>

// # 입력: 
// n -> int: 양의 정수
//
// # 출력:
// answer -> vector<vector<int>>
// : 1부터 n^2까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 2차원 배열
//
// # 고찰:
// 어차피 최대 크기가 30*30 = 900이므로, 단순히 순회하면 쉽게 풀 수 있을 듯 하다
//
// # 설계:
// 1. 행, 열의 현재를 저장하는 crt_point를 생성한다
// 2. 주어진 방향으로 index를 계속 올려가며 vector의 해당 index 위치의 값을 증가시키되, 다음 두 가지 조건
// 2-1. 행, 열의 최대 또는 최소 범위를 넘어갈 경우
// 2-2. 0이 아닌 값에 접근하게 될 경우
// -> 에 맞딱뜨리면 다음 방향으로 이동하도록 한다.

using namespace std;

vector<vector<int>> solution(int n) {
    // 초기값이 0인 n*n 크기의 vector 생성
    vector<vector<int>> answer(n, vector<int>(n, 0));
    
    // crt_point
    pair<int, int> crt_point = {0, 0};
    
    // directions: 우, 하, 좌, 상
    vector<pair<int, int>> directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    int idx = 0;
    auto next = [&](int step = 1) {
        idx = (idx+step + directions.size()) % directions.size();
        return directions[idx];
    };
    
    for (int count = 1; count <= n*n; count++) {
        // 현재 칸에 count 기록
        int cx = crt_point.first;
        int cy = crt_point.second;
        answer[cy][cx] = count;
        
        // 다음 칸 지정
        int dx = directions[idx].first;
        int dy = directions[idx].second;
        int sx = cx+dx;
        int sy = cy+dy;
        
        // 범위를 벗어나지 않고, 다음 칸이 이미 밟지 않은 칸이라면 그대로 진행
        if ((0 <= sx && sx < n) && (0 <= sy && sy < n) && answer[sy][sx] == 0) {
            crt_point = make_pair(sx, sy);
        }
        // 범위를 벗어나거나 다음 칸이 이미 순회한 칸이라면 다음 방향으로 전환하여 진행한다
        else {
            next();
            crt_point = make_pair(cx+directions[idx].first, cy+directions[idx].second);
        }
    }
    
    return answer;
}