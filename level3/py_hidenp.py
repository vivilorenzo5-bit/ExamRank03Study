def hidenp(small: str, big: str) -> bool:
    if not small:
        return True
    i = 0
    for char in big:
        if char == small[i]:
            i += 1
            if i == len(small):
                return True
    return False
