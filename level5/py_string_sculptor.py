def string_sculptor(text: str) -> str:
    result = ""
    make_lower = True
    for char in text:
        if char == ' ':
            result += char
            make_lower = True
        elif char.isalpha():
            if make_lower:
                result += char.lower()
            else:
                result += char.upper()
            make_lower = not make_lower
        else:
            result += char
    return result


if __name__ == "__main__":
    print(repr(string_sculptor("hello")))
    print(repr(string_sculptor("Hello World")))
    print(repr(string_sculptor("abc123def")))
    print(repr(string_sculptor("Python3.9!")))
    print(repr(string_sculptor("")))
