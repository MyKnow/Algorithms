import sys
from collections import Counter

input = sys.stdin.readline

# [Int] N, M
# N: 단어의 수, (범위(자연수): 1 ≤ N ≤ 100,000)
# M: 단어 길이 제한, (범위(자연수): 1 ≤ M ≤ 10)
N, M = map(int, input().split())

# [list(int)] words: 길이가 M 이상인 단어를 저장하는 리스트
words = list()

for _ in range(N):
    word = input().strip()
    
    # M보다 짧은 길이의 단어는 고려하지 않는다.
    if (len(word) < M):
        continue
    
    # M 이상인 단어는 단어장에 추가한다.
    words.append(word)
    
# 3. 알파벳 사전 순으로 오름차순 정렬한다.
words.sort()

# 2. 길이 순으로 내림차순 정렬한다.
words.sort(key=lambda word: len(word), reverse=True)


# [Counter] cntOfWords: 단어장 카운터
cntOfWords = Counter(words)

# [list(str)] result: 결과
result = list()

# 1. 빈도 순으로 내림차순 정렬하여 출력한다.
for key, value in cntOfWords.most_common():
    result.append(key)
    
print("\n".join(result))