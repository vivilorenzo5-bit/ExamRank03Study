def whisper_cipher(text: str, shift: int) -> str:
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "abcdefghijklmnopqrstuvwxyz".upper()

    shift = shift % 26
    s_lower = lower[shift:] + lower[:shift]
    s_upper = upper[shift:] + upper[:shift]

    trans = str.maketrans(lower + upper, s_lower + s_upper)
    return text.translate(trans)


if __name__ == "__main__":
    print(repr(whisper_cipher("hello", 3)))         # "khoor"
    print(repr(whisper_cipher("Hello World!", 1)))  # "Ifmmp Xpsme!"
    print(repr(whisper_cipher("xyz", 3)))           # "abc"
    print(repr(whisper_cipher("ABC123def", 5)))     # "FGH123ijk"
    print(repr(whisper_cipher("", 10)))             # ""
    print(repr(whisper_cipher("abc", -3)))          # "xyz"
