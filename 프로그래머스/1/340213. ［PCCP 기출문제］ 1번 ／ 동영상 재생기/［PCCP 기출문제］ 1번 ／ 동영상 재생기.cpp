#include <string>
#include <vector>
#include <tuple>
#include <sstream>
#include <iostream>

using namespace std;

// # 요약: 동영상 재생기 구현
// - 동영상 재생기의 기능
//      1. "prev": 10초 전으로 이동
//              1-1. 현재 위치가 10초 미만일 경우 영상의 처음 위치(0분 0초)로 이동
//      2. "next": 10초 후로 이동
//              2-1. 남은 영상 시간이 10초 미만일 경우 마지막 시간으로 이동
//      3. op 건너뛰기: 현재 재생 위치가 오프닝 구간(op_start <= now <= op_end)일 때 자동으로 op_end로 시간 이동
//
// # 입력:
// - 형식이 string("mm:ss")인 입력 
//      - video_len -> string("mm:ss"): 비디오 길이
//      - pos -> string("mm:ss"): 기능이 수행되기 직전의 재생 위치
//      - op_start -> string("mm:ss"): 오프닝 시작 시각
//      - op_end -> string("mm:ss"): 오프닝 끝 시각
// - 기타 입력
//      - commands -> vector<string>: 사용자의 입력을 나타내는 1차원 문자열 배열
//              - 길이: 1 <= commands.size() <= 100
//              - 원소: "prev" 또는 "next"
//
// - 형식 string("mm:ss")의 특징
//      1. mm, ss의 범위: 0 <= mm, ss <= 59 (60진법)
//      2. mm 또는 ss가 한 자리일 경우, 앞에 0을 붙여 두자리로 나타낸다.
//      3. 항상 문자열의 길이는 5로 동일하다.
//
// # 출력:
// - result -> string("mm:ss"): 사용자의 입력이 모두 끝난 후 동영상의 위치
//
// # 분석:
// - 예제를 보면, 구현할 기능인 "prev", "next", "오프닝 스킵" 이외엔 시간이 따로 흐르지 않는다.
// - mm과 ss는 60진법을 준수해야 하나, mm은 2자리를 초과할 경우가 없다.
// 
// # 기능 요구사항
// 1. ss가 60 이상이 되면 m을 1 증가 시키고, ss를 60으로 나눈 나머지로 업데이트 하는 기능이 필요하다.
// 2. op 스킵 기능을 위해, "현재 시간"이 op_start와 op_end 사이에 존재하는 지 확인하고, 
//    "현재 시간" 또는 "op_end"를 반환하는 기능이 필요하다.
// 3. "next"나 "prev"로 인해 "현재 시간"이 "00:00~video_len"의 범위를 벗어난다면, 조건에 맞게 조절하는 기능이 필요하다.
// 4. 계산과 출력의 편의를 위해, string("mm:ss")를 pair<int, int>로 변환하고, <int, int>를 string("mm:ss")로 
//    변환하는 기능이 필요하다.


// convert_time_to_int: string("mm:ss") 형태의 시각을 int(초)로 변환하는 함수
int convert_time_to_int(string original) {
    stringstream stream(original);
    string token;
    vector<string> tmp;
    int mm, ss;
    
    while (getline(stream, token, ':')) {
        tmp.push_back(token);
    }
           
    return (stoi(tmp[0]) * 60) + stoi(tmp[1]);
}

// convert_time_to_string: int(초) 형태의 시각을 string("mm:ss")로 변환하여 반환
string convert_time_to_string(int original) {  
    int mm = original / 60;
    int ss = original % 60;
    
    string mm_str = to_string(mm);
    mm_str = (mm_str.size() == 1 ? "0" : "") + mm_str;
    string ss_str = to_string(ss);
    ss_str = (ss_str.size() == 1 ? "0" : "") + ss_str;
    
    return mm_str+":"+ss_str;
}


string solution(string video_len, string pos, string op_start, string op_end, vector<string> commands) {
    int v_len_int = convert_time_to_int(video_len);
    int pos_int = convert_time_to_int(pos);
    int start_int = convert_time_to_int(op_start);
    int end_int = convert_time_to_int(op_end);
    
    for (const auto &command: commands) {
        // 사전 검사
        if (start_int <= pos_int && pos_int <= end_int) {
            pos_int = end_int;
        }
        
        // command 실행
        if (command == "next") {
            pos_int += 10;
        } else {
            pos_int -= 10;
        }
        
        // 이동 후 검사
        if (start_int <= pos_int && pos_int <= end_int) {
            pos_int = end_int;
        }
        
        // 범위 확인
        if (pos_int < 0) {
            pos_int = 0;
        } else if (pos_int > v_len_int) {
            pos_int = v_len_int;
        } 
    }
    
    return convert_time_to_string(pos_int);
}