def solution(lottos, win_nums):
    
    ranking = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} #로또 순위표
    
    none = lottos.count(0) #알아볼 수 없는 번호 갯수
    equal = 0 #일치하는 번호 갯수
    for wn in win_nums: 
        if wn in lottos:
            equal += 1
    
    best = ranking[equal+none] #최고 등수
    lowest = ranking[equal] #죄저 등수
    answer = [best, lowest]
    
    return answer