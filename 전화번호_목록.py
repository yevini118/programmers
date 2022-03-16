def solution(phone_book):
    
    answer = True
    phone_book = sorted(phone_book)
    
    for i in range(0,len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if (phone_book[j].startswith(phone_book[i])):
                answer = False
                return answer
            else:
                break
            
    return answer


def solution(phone_book):
    
    answer = True
    phone_book = sorted(phone_book)
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if(p2.startswith(p1)):
            answer = False
            break
            
    return answer