def solution(n, stations, w):
    answer = 0

    full = [[0,0]]
    empty = []
    
    for s in stations:
        start, end = s-w-1, s+w - 1
        if start < 0:
            start = 0
        if end >= n:
            end = n - 1
        full.append([start, end])
    full.append([n-1,n-1])
    
    
    for i in range(len(full)-1):

        length = full[i+1][0] - full[i][1]
        if i !=0 and i != len(full)-2:
            length -=1
            
        if length > 0:
            empty.append(length)
            

    reach = 2 * w + 1            
    for e in empty:
        if e % reach == 0:
            answer += e // reach
        else:
            answer += e // reach + 1
    
    return answer