def solution(clothes):
    
    ctypes = set(clothe[1] for clothe in clothes)

    clothes_set = {ctype:[] for ctype in ctypes}

    for clothe in clothes:
        clothes_set[clothe[1]].append(clothe[0])

        
    answer = 1
    for values in clothes_set.values():
        answer *= len(values)+1
    
    return answer-1