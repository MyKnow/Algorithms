# [int] N: 입력 받을 단어의 개수 (범위(자연수): 1 ≤ N ≤ 20,000)
N = int(input())

# [set(str)] setOfWords: 입력 받은 단어들을 중복없이 저장하는 집합 (길이: <= N)
setOfWords = set([input() for _ in range(N)])
                 
# [list(str)] setOfWords를 길이 짧은 순, 사전 순으로 정렬한 리스트
sortedList = sorted(setOfWords, key= lambda x: (len(x), x))
                 
print("\n".join(sortedList))