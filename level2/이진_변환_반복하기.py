import re

def solution(s):

    count = 0
    zero = 0

    while(s != "1"):

        before = len(s)
        s = re.sub('0', '', s) #문자열에서 0제거
        after = len(s)
        zero += before - after #제거한 0의 갯수를 더함

        s = format(len(s), 'b') #c를 2진법 문자열로 표현
        count += 1

    return [count, zero]