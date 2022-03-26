from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        
        top = prices.popleft()
        
        sec = 0
        for price in prices:
            sec += 1
            if price < top:
                break

        answer.append(sec)
        
    return answer