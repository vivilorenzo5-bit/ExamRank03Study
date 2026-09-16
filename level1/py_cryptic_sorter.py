def cryptic_sorter(strings: list[str]) -> list[str]:
    def get_key(s: str):
        vowels = sum(1 for char in s.lower() if char in "aeiou")
        return (len(s), s.lower(), vowels)
    res = strings.copy()
    n = len(res)
    for i in range(n):
        for j in range(0, n - i - 1):
            if get_key(res[j]) > get_key(res[j + 1]):
                res[j], res[j + 1] = res[j + 1], res[j]
    return res


if __name__ == "__main__":
    test1 = ["banana", "laranja", "abacate", "morango", "a"]
    print(cryptic_sorter(test1))

    test2 = ["Cat", "cat", "BAT", "dog"]
    print(cryptic_sorter(test2))
