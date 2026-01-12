from collections import deque
import sys 
input = sys.stdin.readline
# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
# 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.
# 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
# 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

# 예제 입력 값 
# 6
# (())())
# (((()())()
# (()())((()))
# ((()()(()))(((())))()
# ()()()()(()()())()
# (()((())()(
        
# 예제 출력 값 
# NO
# NO
# YES
# NO
# YES
# NO

T = int(input().strip())
for _ in range(T):
    s =input().strip()
    result_lst = []
    ok = True
    
    for exp in s:
        if exp == "(":
            result_lst.append(exp)
        else:
            if result_lst:
                result_lst.pop()
            else:
                ok = False
                break
    
    # list에 어떤게 들어있으면 False 반환         
    if result_lst:
        ok = False

    if ok:
        print("YES")
    else:
        print("NO")
        
            


