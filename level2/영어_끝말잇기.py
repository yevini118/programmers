def solution(n, words):

    for i in range(1, len(words)):
        prev_word = words[i-1]
        next_word = words[i]
        if ((prev_word[-1] != next_word[0]) or next_word in words[:i-1]):
            return [(i%n)+1, (i//n)+1]

    return [0,0]


    