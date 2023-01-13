from collections import Counter

def solution(k, tangerine):
    
    answer = 0
    
    tangerine_count = list(Counter(tangerine).values()) #귤 종류별 count
    tangerine_count.sort(reverse = True)
    
    while(k > 0):
        k -= tangerine_count[answer]
        answer += 1
    
    return answer