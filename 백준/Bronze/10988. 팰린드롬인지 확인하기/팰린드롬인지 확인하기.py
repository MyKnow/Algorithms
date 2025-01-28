# [string] word : 알파벳 소문자로만 이루어진 단어 (길이: 1 <= len <= 100)
word = input()

# [string] reversedWord : word를 뒤집은 단어
reversedWord = word[::-1]

# 두 word가 일치하면 1, 아니면 0을 출력한다.
print(1 if (word == reversedWord) else 0)