def solution(genres, plays):
    genres_count = {}
    plays_count = {}
    answer = []
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genres_count:
            genres_count[genre] = 0
        if genre not in plays_count:
            plays_count[genre] = []
        genres_count[genre] += play
        plays_count[genre].append([play, -idx])
        
    genres_list = sorted(genres_count, key=lambda x: genres_count[x])[::-1]
    
    for genre in genres_list:
        plays_count[genre].sort()
        if len(plays_count[genre]) <= 1:
            answer.append(-plays_count[genre].pop()[1])
        else:
            answer.append(-plays_count[genre].pop()[1])
            answer.append(-plays_count[genre].pop()[1])

    return answer