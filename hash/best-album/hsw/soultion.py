from collections import defaultdict
from typing import TypedDict


class GenreType(TypedDict):
    """
    1. `GenreType`을 정의
    """

    total: int
    songs: list[tuple[int, int]]


def solution(genres, plays):
    answer = []

    """
    2. 타입에 맞게 원본 데이터 가공
    """
    dd: defaultdict[str, GenreType] = defaultdict(lambda: {"total": 0, "songs": []})
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        dd[genre]["total"] += play
        dd[genre]["songs"].append((idx, play))

    """
    3. 필요한 순서대로 정렬
    """
    sorted_dd = sorted(dd.items(), key=lambda item: -item[1]["total"])

    for genre_name, genre_dict in sorted_dd:
        sorted_songs = sorted(genre_dict["songs"], key=lambda song: (-song[1], song[0]))
        answer.extend([song[0] for song in sorted_songs[:2]])

    return answer


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    answer = solution(genres, plays)
    print("answer:", answer)
