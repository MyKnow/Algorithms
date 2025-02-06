# [int] N, M: 집합 S에 포함되어 있는 문자열 개수와 검사 대상인 문자열 개수 (범위(자연수): 1 <= N, M <= 10,000)
N, M = map(int, input().split())

# [set(str)] setOfWords: N개의 문자열을 저장할 집합 (크기: N)
setOfWords = set()

for _ in range(N):
    setOfWords.add(input())
    
# [list(str)] listOfWords: M개의 문자열을 저장할 리스트 (크기: M)
listOfWords = []
for _ in range(M):
    listOfWords.append(input())

# [int] count: 집합 S에 포함된 단어의 개수를 저장하는 변수
count = 0

for word in listOfWords:
    if (word in setOfWords):
        count+=1

print(count)