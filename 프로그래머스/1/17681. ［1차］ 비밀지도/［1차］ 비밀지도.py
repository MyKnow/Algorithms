# n -> int: 정사각형 한 변의 길이
# arr1, arr2 -> list(list(int)): 지도를 표현하는 1차원 정수 배열

def solution(n, arr1, arr2):
    answer = []
    
    for i, j in zip(arr1, arr2):
        # 1. 주어진 정수를 이진수로 변환하여
        # 2. 1에 해당하는 부분을 #, 0에 해당하는 부분을 공백으로 바꾼 string을 생성하고
        # 3. answer에 삽입해야 함.
        result = bin(i | j) # -> 0bxxxxx
        
        str_result = result[2:] # -> xxxxx
        str_result = str_result.zfill(n) # -> 0xxxxx
        str_result = str_result.replace("1", "#").replace("0", " ") # -> #  #  
            
        answer.append(str_result)
        
    return answer