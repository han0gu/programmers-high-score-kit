
def solution(genres, plays):
    album = {}
    """
    album = {
        "classic": {
            "total_plays": 1450,
            "songs": [(0, 500), (2, 150), (3, 800)]
        },
        "pop": {
            "total_plays": 3100,
            "songs": [(1, 600), (4, 2500)]
        }
    }
    """
    for i in range(len(genres)):
        if genres[i] in album:
            album[genres[i]]["total_plays"] += plays[i]
            album[genres[i]]["songs"].append((plays[i], i))
        else:
            album[genres[i]] = {"total_plays": plays[i], "songs": [(plays[i], i)]}
    """
    정렬해야함. 
    1. total_palys 내림차순 정렬
    2. songs 의 plays 내림차순 정렬
        - plays 같은 경우 index 오름차순정렬
    """
    
    album = sorted(album.values(), key=lambda x: x["total_plays"], reverse=True)
    """[{"total_plays":3100,"songs":[[600,1],[2500,4]]},{"total_plays":1450,"songs":[[500,0],[150,2],[800,3]]}]"""
    
    for i in album:
        i["songs"].sort(key=lambda x: (-x[0], x[1]))
    """[{"total_plays":3100,"songs":[[2500,4],[600,1]]},{"total_plays":1450,"songs":[[800,3],[500,0],[150,2]]}]"""
    top_songs=[]
    answer=[]
    for i in album:
        top_songs.append(i["songs"][:2])
    """[[[2500,4],[600,1]],[[800,3],[500,0]]]"""
    for song in top_songs:
        for i in song:
            answer.append(i[1])
    return answer