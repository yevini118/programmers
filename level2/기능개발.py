import math

def solution(progresses, speeds):
    
    answer = []
    days = [math.ceil((100 - progresses[i])/speeds[i]) for i in range(len(progresses))]
    days.reverse()

    while(days):

        top = days.pop()
        count = 1
        while(days and top >= days[-1]):
            days.pop()
            count += 1

        answer.append(count)
        
    return answer
        