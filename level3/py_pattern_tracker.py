def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        c1 = text[i]
        c2 = text[i + 1]

        if '0' <= c1 <= '9' and '0' <= c2 <= '9':
            if int(c2) == int(c1) + 1:
                count += 1
    return count


if __name__ == "__main__":
    print(pattern_tracker("123"))          # 2
    print(pattern_tracker("12a34"))        # 2
    print(pattern_tracker("987654321"))    # 0
    print(pattern_tracker("01234567"))     # 7
    print(pattern_tracker("abc"))          # 0
    print(pattern_tracker("1a2b3c4"))      # 0
    print(pattern_tracker("112233"))       # 2
