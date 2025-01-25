# input()은 EOF를 받으면 에러를 발생시키므로, try: except로 예외처리
while True:
    try:
        print(input())
    except EOFError:
        break