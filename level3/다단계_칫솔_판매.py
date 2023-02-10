def solution(enroll, referral, seller, amount):
    
    money = [amount[i] * 100 for i in range(len(amount))] #판매금액
    profits = {enroll[i]:0 for i in range(len(enroll))} #수익
    organization = {enroll[i]:referral[i] for i in range(len(enroll))} #조직도
    
    for i in range(len(seller)):
        
        s = seller[i] #판매원
        r = organization[s] #추천인
        p = money[i] #판매금액
        
        while(p >= 1):
            
            profit = p // 10 #추천인의 수익
            profits[s] += round(p - profit) #판매원이 갖는 수익
            
            if r == '-':
                break
            
            s = r
            r = organization[s]
            p = profit
        
    return list(profits.values())