def solution(phone_book):
    if len(phone_book) == 1:
        return True

    phone_book.sort(key=int)

    d = {phone_book[0]: 1}

    for phone in phone_book[1:]:
        for i in range(1, len(phone)):
            target = phone[:i]

            if d.get(target):
                return False

        d[phone] = 1

    return True
