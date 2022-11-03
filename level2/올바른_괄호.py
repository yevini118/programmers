def solution(s):
    
    bracket = []
    
    if s.startswith(')'):
        return False
    
    for i in range(0, len(s)):
        if s[i] == '(':
            bracket.append(s[i])
        elif s[i] == ')' and bracket:
            bracket.pop()
    
    return False if bracket else True