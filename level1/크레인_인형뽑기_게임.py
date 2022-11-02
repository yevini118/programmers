def solution(board, moves):

    bucket = []
    answer = 0

    for m in moves:
        for i in range(len(board)):
            target = board[i][m-1]
            if target == 0: #빈칸인 경우 넘어감
                continue
            else:
                bucket.append(target) #집어 올린 인형을 바구니에 넣음
                board[i][m-1] = 0 #해당 칸을 빈칸으로 변경
                break

        if len(bucket)>=2 and bucket[-1] == bucket[-2]: #같은 모형 인형 두 개가 바구니에 쌓인 경우
            bucket.pop()
            bucket.pop() #인형 두 개를 없앰
            answer += 2 #사라진 인형의 개수 +2

    return answer  