from collections import deque
import sys 
input = sys.stdin.readline

n, w, l = map(int, input().split())
a = list(map(int, input().split()))
time = 0
result_lst = []
print(f"트럭의 수 = {n}, 다리의 길이 = {w}, 최대 하중 = {l}")
# print(f"각 트럭의 무게들 = {a}")

# 다리의 길이는 w 단위길이(unit distance)이며,
# 각 트럭들은 하나의 단위시간(unit time)에 하나의 단위길이만큼만 이동할 수 있다고 가정한다

# 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다.
# 참고로, 다리 위에 완전히 올라가지 못한 트럭의 무게는 다리 위의 트럭들의 무게의 합을 계산할 때 포함하지 않는다고 가정한다.

# 1. 현재 다리위의 트럭 무게와 다음으로 올라갈 트럭의 무게를 비교

n_weight = deque((a))
print(f"각 트럭의 무게를 담음 = {n_weight}")
bridge = deque([0] * w)

while n_weight or sum(bridge) > 0:
    time += 1
    bridge.popleft()
    if n_weight and (sum(bridge) + n_weight[0] <= l):
        bridge.append(n_weight.popleft())   # 트럭 올리기
    else:
        bridge.append(0)
print(time)

    
    


  







