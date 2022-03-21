import math

def solution(progresses, speeds):
    
    answer = []
    days = [math.ceil((100 - progresses[i])/speeds[i]) for i in range(len(progresses))] #개발일수
    days.reverse()

    while(days):

        top = days.pop() #앞에있는 기능
        count = 1
        while(days and top >= days[-1]): #뒤에있는 기능중 개발 완료된 기능
            days.pop()
            count += 1

        answer.append(count)
        
    return answer
        