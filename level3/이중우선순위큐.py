import heapq

def solution(operations):
    
    heap = []
    
    for o in operations:
        o = o.split()
        
        if o[0] == 'I': #큐에 주어진 숫자를 삽입
            heap.append(int(o[1]))
            
        elif o[0] == 'D': 
            if not heap:
                continue
            if o[1] == '1': #큐에서 최댓값을 삭제
                heap.sort()
            elif o[1] == '-1': #큐에서 최솟값을 삭제
                heap.sort(reverse=True)
            heap.pop()

    return [0,0] if not heap else [max(heap), min(heap)]