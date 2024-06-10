from collections import deque

def q2(s):
    stack = deque()
    res = [' '] * len(s)
    size = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
            size += 1
        elif char == ')':
            if size != 0:
                stack.pop()
                size -= 1
            else:
                res[i] = '?'
    
    while size != 0:
        res[stack.pop()] = 'x'
        size -= 1
    

    return s + '\n' + ''.join(res)
