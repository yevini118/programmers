import re

def solution(record):
    
    answer = []
    records = [] #입퇴장기록 list
    nickname = {} #닉네임 dictionary
    
    for r in record:
        r = re.split(' ', r)
        if r[0].startswith('E'): #입장의 경우
            nickname[r[1]] = r[2] #닉네임 정보를 추가
            records.append(r) #입퇴장기록 추가
        elif r[0].startswith('C'): #닉네임 변경의 경우
            nickname[r[1]] = r[2] #닉네임 정보를 수정
        else: #퇴장의 경우
            records.append(r) #입퇴장 기록 추가
    
    for r in records:
        if r[0].startswith('E'):
            answer.append(f'{nickname[r[1]]}님이 들어왔습니다.') #유저 아이디에 해당하는 닉네임 출력
        else:
            answer.append(f'{nickname[r[1]]}님이 나갔습니다.')
            
    return answer