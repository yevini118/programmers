def solution(A, B):
    
    answer = 0
    A.sort()
    B.sort()
    
    for i in range(len(A)-1, -1, -1):
        if B:
            if B[-1] > A[i]:
                answer += 1
                B.pop()
                
    return answer