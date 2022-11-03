from collections import Counter

def solution(id_list, report, k):
    
    report_set = [r.split(" ") for r in set(report)] #report의 set
    report_count = Counter([r[1] for r in report_set]) #유저별 신고당한 횟수
    
    mail_count = {id:0 for id in id_list} #0으로 초기화된 메일 전송 횟수 set
    for r in report_set:
        if report_count[r[1]] >= k: #신고한 유저가 정지 당한 경우
            mail_count[r[0]] += 1 #메일 전송 count

    return list(mail_count.values())