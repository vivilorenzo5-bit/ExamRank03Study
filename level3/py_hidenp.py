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


if __name__ == "__main__":
    print(hidenp("abc", "a1b2c3"))
    print(hidenp("ace", "abcde"))
    print(hidenp("aec", "abcde"))
    print(hidenp("", "abc"))
    print(hidenp("abc", "ab"))
    print(hidenp("aaaa", "aaa"))
    print(hidenp("sing", "subsequence testing"))
