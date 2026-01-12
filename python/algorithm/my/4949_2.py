# 딕셔너리 활용
import sys
input = sys.stdin.readline
from collections import deque

for input in sys.stdin:

    braket_dic = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
        '>' : '<'
    }
    
    stack = deque()
    open_braket = set(braket_dic.values())
    close_braket = braket_dic.keys()
    ok = True

    s = input.rstrip('\n')

    if s == '.':
        break
    
    for exp in s:
        if exp in open_braket:
            stack.append(exp)
            
        elif exp in close_braket:
            if stack and stack[-1] == braket_dic[exp]:
                stack.pop()
            else:
                ok = False
                break
            
    if not stack and ok:
        print("yes")
    else:
        print("no")
                
            
    
