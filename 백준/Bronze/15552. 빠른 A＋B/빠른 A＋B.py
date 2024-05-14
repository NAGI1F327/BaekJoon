import sys   # sys를 포함하겠다는 것 ,sys.stdin.readline()을 사용 할 수 있도록 함

T = int(input())

i = 0
while i < T:
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
    i += 1

# sys.stdin.readline()
# C는 그 자체로도 빠르기 때문에 별 다른 조치를 취하지 않아도 되지만,
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
# 또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 
# 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.