from functools import cmp_to_key
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
    dd = {}
    for genre in set(genres):
        dd[genre] = {"total": 0, "songs": []}

    for idx, genre in enumerate(genres):
        dd[genre]["total"] += plays[idx]
        dd[genre]["songs"].append((idx, plays[idx]))

    """
    3. 필요한 순서대로 정렬
    """
    sorted_by_total = dict(
        sorted(dd.items(), key=cmp_to_key(compare_genre), reverse=True)
    )

    for value in sorted_by_total.values():
        songs = value["songs"]
        sorted_by_plays = sorted(songs, key=cmp_to_key(compare_songs), reverse=True)
        answer.extend([t[0] for t in sorted_by_plays[:2]])

    return answer


def compare_genre(g1: tuple[str, GenreType], g2: tuple[str, GenreType]) -> int:
    return g1[1]["total"] - g2[1]["total"]


def compare_songs(s1: tuple[int, int], s2: tuple[int, int]) -> int:
    return s1[1] - s2[1]


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
answer = solution(genres, plays)
print("answer:", answer)
