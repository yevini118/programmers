from collections import deque

def solution(rows, columns, queries):
    
    answer = []
    board = [[i + j * columns  for i in range(1, columns+1)] for j in range(rows)]

    for x1, y1, x2, y2 in queries:
        
        x = x2 - x1
        y = y2 - y1

        points = [] #테두리 영역
        
        for i in range(y):
            points.append([x1, y1 + i])
        for i in range(x):
            points.append([x1 + i, y2])
        for i in range(y):
            points.append([x2, y2 - i])
        for i in range(x):
            points.append([x2 - i, y1])
        
        nums = deque([]) #테두리 안의 숫자
        for p in points:
            nums.append(board[p[0]-1][p[1]-1])
        
        answer.append(min(nums)) #테두리 안의 숫자중 최소값
        nums.rotate(1) #시계방향으로 한칸씩 회전
                
        for i in range(len(points)): #행렬에 테두리 회전 적용
            board[points[i][0] -1][points[i][1] -1] = nums[i]

    return answer  