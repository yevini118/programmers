def solution(s):
    
    answer = len(s)
    for i in range(1, len(s)//2+1):
        result = "" #압축된 문자열
        count=1
        source = s
        
        while (len(source)>=i):
            pattern = source[0:i] #압축단위 문자
            source = source[i:] 

            if source.startswith(pattern): #문자가 반복될 경우
                count += 1
            else: #문자가 반복되지 않을 경우
                temp = str(count) + pattern if count>1 else pattern
                result += temp
                count = 1
                
        result += source
        if len(result)<answer:
            answer = len(result)

    return answer