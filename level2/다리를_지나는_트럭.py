from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    answer = 1 #sec

    truck_weights = deque(truck_weights)
    on_weight = truck_weights.popleft() #다리 위 트럭무게의 합
    on_trucks = deque([[on_weight, 0]]) #다리 위의 트럭
    
    while(on_trucks): 
        
        answer += 1

        for truck in on_trucks:
            truck[1] += 1
        
        if (on_trucks[0][1] == bridge_length): 
            on_weight -= on_trucks.popleft()[0]

        if (truck_weights and on_weight+truck_weights[0] <= weight):
            on_weight += truck_weights[0]
            on_trucks.append([truck_weights.popleft(), 0])
            
    return answer