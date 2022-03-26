from heapq import heappop,heappush,heapify

def solution(scoville, K):
    
    heapify(scoville)
    answer = 0
    
    while len(scoville) > 1 and scoville[0] < K:
        
        new_scoville = heappop(scoville) + heappop(scoville) * 2
        heappush(scoville, new_scoville)
        
        answer += 1
    
    if scoville.pop() < K:
        answer = -1
        
    return answer