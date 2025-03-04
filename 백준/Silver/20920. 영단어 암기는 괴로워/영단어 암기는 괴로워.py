import sys
from collections import Counter

input = sys.stdin.readline

# [Int] N, M
N, M = map(int, input().split())

# [Counter] cntOfWords: 단어 빈도 저장
cntOfWords = Counter()

for _ in range(N):
    word = input().strip()
    
    if len(word) >= M:  # M 이상 길이만 저장
        cntOfWords[word] += 1

# 단어 정렬 (빈도, 길이, 알파벳 순)
sorted_words = sorted(cntOfWords.keys(), key=lambda word: (-cntOfWords[word], -len(word), word))

# 한 번에 출력
sys.stdout.write("\n".join(sorted_words) + "\n")