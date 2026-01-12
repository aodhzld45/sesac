# 예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다
# 백준용 입력 모듈
import sys 
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
q = deque(range(1, n+1))

dump_card = []

while len(q) > 1:
    dump_card.append(q.popleft())
    q.append(q.popleft())

last_card = q[0]

dump_card.append(last_card)

print(*dump_card)


# 첫째 줄에 버리는 카드들을 순서대로 출력한다. 제일 마지막에는 남게 되는 카드의 번호를 출력한다.






