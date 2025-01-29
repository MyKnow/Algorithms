# [string] croatiaString : 크로아티아 알파벳이 포함되어 있을 수도 있는 문자열 (길이: 최대 100 단어)
croatiaString = input()

# [list(string)] croatiaTable : 크로아티아 알파벳을 정리해놓은 리스트
croatiaTable = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

# 크로아티아 알파벳을 전부 '*' 한 글자로 치환함.
for croatiaAlphabet in croatiaTable :
    croatiaString = croatiaString.replace(croatiaAlphabet, "*")
        
# *이 추가된 croatiaString의 길이를 더한 값을 출력한다.
print(len(croatiaString))