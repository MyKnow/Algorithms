#include <string>
#include <vector>
#include <map>
#include <tuple>
#include <sstream>
#include <iostream>

using namespace std;

// # 입력:
// - friends -> vector<string>
// : 친구들의 이름을 담은 1차원 string vector 
//      - 길이: 2 <= friends.size() <= 50
//      - 원소: friends의 원소.size() <= 10
//
// - gifts -> vector<string>
// : 이번 달까지 친구들이 주고 받은 선물 기록을 담은 1차원 string vector
//      - 길이: 1 <= gifts.size() <= 10,000
//      - 원소: "{선물을 준 친구의 이름} {선물을 받은 친구의 이름}"으로, 각 이름이 공백으로 구분됨
//          - 두 이름이 같은 경우는 존재하지 않음!!
// # 출력:
// - answer -> int
// : 다음 달에 가장 많은 선물을 받는 친구가 받을 선물의 수
//
// # 규칙:
// 1. 두 사람이 선물을 주고 받은 기록이 있다면, 
// 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
//
// 2. 기록이 없거나 횟수가 같다면, "선물 지수"가 더 큰 사람이 더 작은 사람에게 선물을 하나 받습니다.
// 2-1. "선물지수": 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값

int solution(vector<string> friends, vector<string> gifts) {
    int answer = 0;
    
    // 규칙 적용 전의 로그 기록 변수
    // detail_log: {준 사람, {받은 사람, 준 횟수}}
    // numeric_log: {사람, {준 횟수, 받은 횟수}}
    map<string, map<string, int>> detail_log;
    map<string, pair<int, int>> numeric_log;
    
    // 1. 두 자료 업데이트
    for (const auto &gift: gifts) {
        // 공백을 기준으로 주고 받은 사람 분리
        stringstream ss(gift);
        string giver, receiver;
        ss >> giver >> receiver;
        
        // 1-1. detail_log 업데이트
        detail_log[giver][receiver] += 1;
        
        // 1-2. numeric_log 업데이트
        numeric_log[giver].first += 1;
        numeric_log[receiver].second += 1;
    }
    
    // 2. friends를 중복 제거 순회하며 서로의 선물 횟수를 대조 및 result를 업데이트 한다
    map<string, int> result;
    for (int i = 0; i < friends.size(); i++) {
        for (int j = i+1; j < friends.size(); j++) { 
            string giver_name = friends[i], receiver_name = friends[j];
            // gaved_count: giver_name이 receiver_name에게 선물 준 횟수
            int gaved_count = detail_log[giver_name][receiver_name];
                
            // received_count: giver_name이 receiver_name에게 선물 받은 횟수
            int received_count = detail_log[receiver_name][giver_name];
                        
            // 2-1. 선물을 주고 받은 기록이 있고, count가 같지 않다면, count가 더 높은 사람이 다음 달에 선물을 하나 받는다.
            if (gaved_count != received_count) {
                if (gaved_count > received_count) result[giver_name]++;
                else result[receiver_name]++;
            }
            // 2-2. 주고 받은 기록이 없거나, count가 동일하다면 선물 지수가 더 큰 사람이 작은 사람에게 선물을 하나 더 받는다.
            else {
                // ?_score: 선물 지수
                int giver_score = numeric_log[giver_name].first - numeric_log[giver_name].second;
                int receiver_score = numeric_log[receiver_name].first - numeric_log[receiver_name].second;
                    
                if (giver_score > receiver_score) result[giver_name]++;
                else if (giver_score < receiver_score) result[receiver_name]++;
            }
                
        }
    }
    
    for (const auto& res: result) answer = max(answer, res.second);
    
    return answer;
}