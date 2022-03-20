def solution(genres, plays):
    
    music_dict = {i: [genres[i], plays[i]] for i in range(0,len(plays))}
    genre_sum = {genre : 0 for genre in set(genres)}
    answer = []

    #장르별 총 재생횟수 계산
    for music in music_dict.values():
        genre_sum[music[0]] += music[1] 

    #genre_sum, music_dict 정렬
    genre_sum = dict(sorted(genre_sum.items(), key= lambda k: -k[1]))
    music_dict= dict(sorted(music_dict.items(), key= lambda k: (-k[1][1], k[0])))

    #answer에 장르별 2개씩 추가
    for genre in genre_sum:
        count = 0
        for id, music in music_dict.items():
            if count == 2:
                break
            elif genre == music[0]:
                answer.append(id)
                count += 1

    return answer





