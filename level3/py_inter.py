def inter(s1: str, s2: str) -> str:
    res = ""
    for char in s1:
        if char in s1 and char not in res:
            res += char
    return res


if __name__ == "__main__":
    print(repr(inter("hello", "world")))
    print(repr(inter("banana", "band")))
    print(repr(inter("abcabc", "bc")))
    print(repr(inter("abc", "xyz")))
    print(repr(inter("", "abc")))
