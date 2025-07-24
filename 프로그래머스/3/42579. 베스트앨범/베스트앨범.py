from collections import defaultdict


def solution(genres, plays):
    answer = []
    playsongs = {}
    allsongs  = {}
    for i in range(len(genres)):
        allsongs[genres[i]] = allsongs.get(genres[i], 0) + plays[i]
        playsongs[genres[i]] = playsongs.get(genres[i], []) + [(plays[i], i)]
    print(allsongs)
    
    genSort = sorted(allsongs.items(), key = lambda x: x[1], reverse = True)
    for (genre, totalplay) in genSort:
        playsongs[genre] = sorted(playsongs[genre], key = lambda x : (-x[0], x[1]))
        answer += [idx for (play, idx) in playsongs[genre][:2]]
        
    print(playsongs)
    print(genSort)
    # print(sorted(songs.items(), key = lambda item : sum(item[1].values())))
        

    
    return answer