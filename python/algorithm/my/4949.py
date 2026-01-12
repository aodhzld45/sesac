import sys
input = sys.stdin.readline

for input in sys.stdin:
    
    result_lst = []
    ok = True
    
    s = input.rstrip('\n')
    if s == '.':
        break
    
    for exp in s:
        if exp == "(" or exp == "[" or exp == "{":
            result_lst.append(exp)
        elif exp == ")":
            if not result_lst or result_lst[-1] != "(": # 리스트의 마지막 요소에 ( 열리는 괄호가 들어있으면
                ok = False
                break
            result_lst.pop()
        elif exp == "]":
            if not result_lst or result_lst[-1] != "[":  # 리스트의 마지막 요소에 [ 열리는 괄호가 들어있으면
                ok = False
                break
            result_lst.pop()
        elif exp == "}":
            if not result_lst or result_lst[-1] != "{":
                ok = False
                break
            result_lst.pop()

    if not result_lst and ok:
        print("yes")
    else:
        print("no")