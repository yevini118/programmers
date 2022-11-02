import re

def solution(dartResult):
    
    score = []
    bonus = {'S':1, 'D':2, 'T':3} 
    
    dartResult = re.sub('10','@', dartResult) #10의 경우 @로 치환
    
    for s in dartResult:
        if s.isdecimal(): #0~9의 숫자인 경우 num에 저장
            num = int(s)
        elif s == '@': #@로 치환된 10의 경우 num에 10 저장
            num = 10
        elif s == 'S' or s == 'D' or s == 'T': #보너스 점수 계산
            score.append(num ** bonus[s])
        elif s == '*': #스타상 계산
            score[-1] *= 2
            if len(score) >=2:
                score[-2] *= 2
        elif s == '#' : #아차상 계산
            score[-1] *= -1
    
    return sum(score)