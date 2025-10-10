# * 요약
# - 규칙에 따라 검색어에 대한 웹페이지의 매칭 점수 계산

# * 규칙
# 1. 기본점수, 외부 링크 수, 링크점수, 매칭점수
#   1-1. 기본점수: 웹페이지의 텍스트 중 검색어가 등장하는 횟수(대소문자 무시)
#   1-2. 외부 링크 수: 해당 웹페이지에서 다른 외부 페이지로 연결된 링크의 개수
#   1-3. 링크점수: 해당 웹페이지로 링크가 걸린 다른 웹페이지의 (기본점수 % 외부 링크 수)의 총합
#   1-4. 매칭점수: 기본점수 + 링크점수

# * 입력
# - word: 알파벳 대소문자로 구성된 하나의 영단어 문자열 (길이 1 이상 12 이하)
# - pages: HTML 형식의 웹페이지가 문자열 형태로 들어있는 배열
#   - 배열 길이: 1 이상 20 이하
#   - 문자열 길이: 1 이상 1,500 이하
#   - 웹페이지 url: <head> tag 내에 <meta> tag의 값으로 주어짐
#       - ex) <meta property="og:url" content="https://careers.kakao.com/index" />
#   - 외부 링크: ex) <a href="https://careers.kakao.com/index">

# * 출력
# - 매칭점수가 가장 높은 웹페이지의 index
#   - 여러 개라면, 그 중 번호가 가장 작은 것

# * 주의
# - 검색은 알파벳 대소문자 차이를 무시하되, 단어 단위로 일치해야 한다.
#   - ex) aba -> abab abababab(x), aba@aba aba(3o)

import re

def solution(word, pages):
    word = word.lower()
    
    # url → {index, basic, out_links, score}
    page_info = dict()

    # 1. 각 페이지의 url, 기본점수, 외부링크 추출
    for i, html in enumerate(pages):
        html_lower = html.lower()
        
        # URL 추출
        url = re.search(r'<meta[^>]*property=["\']og:url["\'][^>]*content=["\']([^"\']+)["\']', html_lower).group(1)
        
        # 외부 링크 추출
        out_links = re.findall(r'<a href=["\']([^"\']+)["\']', html_lower)
        
        # 기본 점수 계산
        words = re.findall(r'[a-z]+', html_lower)
        basic_score = sum(1 for w in words if w == word)
        
        page_info[url] = {
            "index": i,
            "basic": basic_score,
            "out_links": out_links,
            "link_score": 0.0
        }

    # 2. 링크점수 계산 (역방향 연결)
    for url, info in page_info.items():
        if len(info["out_links"]) == 0:
            continue
        link_value = info["basic"] / len(info["out_links"])
        for out in info["out_links"]:
            if out in page_info:
                page_info[out]["link_score"] += link_value

    # 3. 매칭점수 계산 및 최고점 페이지 탐색
    max_score, max_index = -1, -1
    for url, info in page_info.items():
        total = info["basic"] + info["link_score"]
        if total > max_score or (total == max_score and info["index"] < max_index):
            max_score, max_index = total, info["index"]
    return max_index