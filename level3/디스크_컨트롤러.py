from heapq import heappush, heappop
from collections import deque

def solution(jobs):
    
    len_jobs = len(jobs) #작업 개수
    jobs = deque(sorted(jobs, key=lambda j: j[0])) 

    processing = jobs.popleft() #첫번째 작업
    wait_jobs = [(processing[1], processing[0])] #작업대기 목록

    answer = 0
    time = 0 #현재 시간
    while (jobs or wait_jobs):
        
        if wait_jobs and time >= wait_jobs[0][1]:
            processing = heappop(wait_jobs)
            time += processing[0]
            answer += (time - processing[1])
        else:
            time += 1
                
        while (jobs):
            if jobs[0][0] <= time:
                job = jobs.popleft()
                heappush(wait_jobs, (job[1], job[0]))
            else :
                break
        
    return int(answer/len_jobs)