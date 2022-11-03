def solution(survey, choices):
    
    score = {1 : 3, 2 : 2 , 3 : 1, 4 : 0, 5 : 1, 6 : 2, 7 : 3} #점수 환산표
    result = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M': 0, 'A' : 0, 'N' : 0} #유형 별 획득 점수
    indicators = [['R','T'],['C','F'],['J','M'],['A','N']] #성격 지표 표
    answer = ''
    
    for i in range(len(survey)): 
        if choices[i] <= 4: #매우 비동의 ~ 모르겠음 의 경우
            result[survey[i][0]] += score[choices[i]] #첫 번째 캐릭터에 점수 부여
        elif choices[i] > 4: #약간 동의 ~ 매우 동의 의 경우 
            result[survey[i][1]] += score[choices[i]] #두 번째 캐릭터에 점수 부여
    
    for i in indicators:
        if result[i[0]] >= result[i[1]]: #지표 중 점수가 더 큰 성격유형을 선택
            answer += i[0]
        else:
            answer += i[1]
            
    return answer