def solution(n, arr1, arr2):

    map_total = [f'{arr1[i]|arr2[i]:016b}'[-n:] for i in range(0, n)] #16자리의 2진수로 만들어 n자리 2진수로 슬라이싱
    answer = []

    for mt in map_total:
        line = mt.replace('0',' ')
        line = line.replace('1', '#')
        answer.append(line)

    return answer

def solution(n, arr1, arr2): #rjust사용
    
    map_total = [f'{arr1[i]|arr2[i]:b}'.rjust(n, '0') for i in range(0, n)]
    answer = [mt.replace('0',' ').replace('1', '#') for mt in map_total]
        
    return answer