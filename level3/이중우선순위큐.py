from heapq import heapify, heappush, heappop
from collections import deque

def solution(operations):
    answer = []
    
    temp = deque([])
    
    
    for operation in operations:
        command = operation[0]
        num = operation[2:]
        
        if command == "I":
            temp.append(num)
            

        elif command == "D" and temp:
            heapify(list(temp))
            queue = []
            while temp:
                queue.append(heappop(temp))
            temp = queue
            
        
            # if num == "1":
            #     temp.popleft()                    
            # elif num == "-1":
            #     temp.pop()
    
    if temp:
        answer = [temp[-1], temp[0]]
    else:
        answer = [0,0]
    return answer

operations = ["I 7","I 5","I -5","D -1"]	
print(solution(operations))