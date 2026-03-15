from typing import TypedDict


class NewSignalType(TypedDict):
    signal: list[int]  # [g, y, r]
    period: int  # r + g + 1
    yellow_band: tuple[int, int]  # (g + 1, g + y)


def solution(signals: list[list[int]]):
    # 중복 지점이 아예 없는 경우
    if there_is_no_answer(signals):
        return -1

    # new type으로 초기화
    new_signals: list[NewSignalType] = []
    for signal in signals:
        new_signal: NewSignalType = {
            "signal": signal,
            "period": signal[2] + signal[0] + 1,
            "yellow_band": (
                signal[0] + 1,
                signal[0] + signal[1],
            ),
        }
        new_signals.append(new_signal)

    # 중복 지점 찾을 때까지 반복
    while True:
        # yellow_band_start_max 구하기
        yellow_band_start_list = [
            new_signal["yellow_band"][0] for new_signal in new_signals
        ]
        yellow_band_start_max = max(yellow_band_start_list)

        # 모든 band의 start를 yellow_band_start_max 이상으로 맞추기
        for new_signal in new_signals:
            start, end = new_signal["yellow_band"]
            g, y, r = new_signal["signal"]
            while start < yellow_band_start_max:
                start = end + new_signal["period"]
                end = start + y - 1
                new_signal["yellow_band"] = (start, end)

        # 모두 중복이면
        if is_dup(new_signals):
            yellow_band_start_list = [
                new_signal["yellow_band"][0] for new_signal in new_signals
            ]
            return max(yellow_band_start_list)


def is_yellow_band_duplicate(
    yellow_band_1: tuple[int, int],
    yellow_band_2: tuple[int, int],
) -> bool:
    start_1, end_1 = yellow_band_1
    start_2, end_2 = yellow_band_2
    return not end_1 < start_2 and not end_2 < start_1


def there_is_no_answer(signals: list[list[int]]) -> bool:
    for i in range(len(signals)):
        signal_1 = signals[i]
        g, y, _ = signal_1
        yellow_band_1 = (g + 1, g + y)

        for j in range(i + 1, len(signals)):
            signal_2 = signals[j]
            g, y, _ = signal_2
            yellow_band_2 = (g + 1, g + y)

            if sum(signal_1) == sum(signal_2) and not is_yellow_band_duplicate(
                yellow_band_1, yellow_band_2
            ):
                return True

    return False


def is_dup(new_signals: list[NewSignalType]) -> bool:
    for i in range(len(new_signals)):
        yellow_band_1 = new_signals[i]["yellow_band"]

        for j in range(i + 1, len(new_signals)):
            yellow_band_2 = new_signals[j]["yellow_band"]

            if not is_yellow_band_duplicate(yellow_band_1, yellow_band_2):
                return False

    return True


if __name__ == "__main__":
    signals = [[2, 1, 2], [5, 1, 1]]
    # signals = [[2, 3, 2], [3, 1, 3], [2, 1, 1]]
    # signals = [[3, 3, 3], [5, 4, 2], [2, 1, 2]]
    # signals = [[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]]

    answer = solution(signals)
    print("\nanswer", answer)
