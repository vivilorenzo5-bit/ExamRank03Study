def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")


def cryptic_sorter(strings: list[str]) -> list[str]:
    res = list(strings)
    n = len(res)
    for i in range(n):
        for j in range(0, n - i - 1):
            key1 = (len(res[j]), res[j].lower(), count_vowels(res[j]))
            key2 = (len(res[j+1]), res[j+1].lower(), count_vowels(res[j+1]))
            if key1 > key2:
                res[j], res[j+1] = res[j+1], res[j]

    return res


if __name__ == "__main__":
    test1 = ["banana", "laranja", "abacate", "morango", "a"]
    print(cryptic_sorter(test1))

    test2 = ["Cat", "cat", "BAT", "dog"]
    print(cryptic_sorter(test2))
