import collections

def solution(priorities, location):
    
    wait_list =  [(i,priorities[i]) for i in range(len(priorities))] #대기목록
    answer = 0
    
    while(len(wait_list) > 0):
        
        top = wait_list[0]
        wait_list = wait_list[1:]
        for wait in wait_list: 
            if top[1] < wait[1]: 
                wait_list.append(top) 
                break
        else:
            answer += 1 
            if top[0] == location: 
                return answer
        
    return answer+1


def solution_2(priorities, location):
    
    wait_list =  collections.deque([(i,priorities[i]) for i in range(len(priorities))]) 
    answer = 0
    
    while(True): #while문 조건변경
        
        top = wait_list.popleft() #deque 사용
        if any(top[1] < wait[1] for wait in wait_list): #any사용
                wait_list.append(top)
        else:
            answer += 1
            if top[0] == location:
                return answer



