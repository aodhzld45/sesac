# 첫째줄에 색종이의 수
n = int(input())

# 둘째줄 한줄에 하나씩 색종이를 붙인 위치
for _ in range(n):
    x, y = map(int, input().split())
    
print(f"색종이의 수 = {n}")

# 가로 세로가 100인 리스트
result_lst = []

for i in range(100):
    line = []
    for j in range(100):
        line.append(0)
    result_lst.append(line)
    
    


