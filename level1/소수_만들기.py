from itertools import combinations

def solution(nums):
    
    answer = 0
    
    num_set = list(combinations(nums, 3)) #가능한 3개수 조합
    for a, b, c in num_set:
        sum = a + b + c # 3개수의 합
        
        for i in range(2, sum):
            if sum % i == 0:
                break
        else:
            answer += 1

    return answer


def solution2(nums):
    
    answer = 0
    
    num_set = list(combinations(nums, 3))
    for a, b, c in num_set:
        sum = a + b + c
        
        for i in range(2, int(sum**(1/2))+1): #제곱근까지만 검사
            if sum % i == 0:
                break
        else:
            answer += 1

    return answer