import re

def solution(new_id):
    
    new_id = re.sub('[^-_.\w\d]','',new_id.lower()) #1, 2단계
    new_id = re.sub( '\.+', '.', new_id) #3단계
    new_id = new_id.strip('.') #4단계
    if len(new_id) == 0: #5단계
        new_id = 'a'
    elif len(new_id) >= 16: #6단계
        new_id = new_id[0:15].rstrip('.')
    
    if len(new_id) <= 2: #7단계
        new_id += new_id[-1] * (3-len(new_id))

    return new_id