from datetime import timedelta, datetime

def solution(n, t, m, timetable):
    
    fmt = "%H:%M" #시간 형식
    term = timedelta(minutes = t) #셔틀 간격
    
    timetable.sort(reverse=True)
    shuttles = [] #셔틀 시간표
    shuttle = datetime(2022,8,25,9,0,0) #첫번째 셔틀

    #셔틀 시간표 생성
    for i in range(0, n):
        shuttles.append(shuttle.strftime(fmt))
        shuttle = shuttle + term
    
    #셔틀 별 탑승크루 파악
    for s in shuttles:
        crew = [] #셔틀 별 탑승크루
        while(len(crew) < m): #m명까지 탑승가능
            if timetable:
                if timetable[-1] <= s: #셔틀도착 시간까지 대기열에 선 경우
                    crew.append(timetable.pop())
                else:
                    break
            else:
                break

    #마지막 셔틀에서 
    if len(crew) == m: #탑승인원이 가득 찬 경우
        last_time = datetime.strptime(crew[-1], fmt) - timedelta(minutes=1) #가장 마지막에 도착한 크루보다 1분 일찍 도착
        answer = last_time.strftime(fmt)
    else: #탑승인원이 가득 차지 않은 경우
        answer = shuttles[-1] #셔틀 도착 시간에 맞춰 도착
    
    return answer

