import re

def solution(skill, skill_trees):
    
    answer = 0

    for s in skill_trees:
        
        s = re.sub('[^' + skill+ ']', '', s)
        if skill.startswith(s):
            answer += 1
    
    return answer