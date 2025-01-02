# listOfRemainder: list - 음이 아닌 정수로 구성된 1000 이하의 자연수를 42로 나눈 값을 저장하는 list
listOfRemainder = []

# 숫자를 입력 받아서 42를 나누고, 이를 list에 insert하는 걸 10번 반복한다.
for _ in range(10):
    # remainder: int - 숫자를 입력 받고 42로 나눈 값 (1 <= remainder <= 1000)
    remainder = int(input()) % 42
    
    # 리스트에 해당 나머지가 존재하지 않으면 값을 추가한다  
    if (remainder not in listOfRemainder) :
        listOfRemainder.append(remainder)

# list의 길이를 출력한다.
print(len(listOfRemainder))