import sys
    
# 총 다섯줄의 입력
# 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸없이    
words = [sys.stdin.readline().rstrip() for _ in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end = "")
            
 
