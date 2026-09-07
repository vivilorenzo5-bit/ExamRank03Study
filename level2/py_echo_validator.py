def echo_validator(text: str) -> bool:
    clean_text = ""
    for char in text:
        if char.isalpha():
            clean_text += char.lower()
    return clean_text == clean_text[::-1]


if __name__ == "__main__":
    print(echo_validator("A man, a plan, a canal: Panama"))
    print(echo_validator("race a car"))
    print(echo_validator("racecar"))
    print(echo_validator("No 'x' in Nixon"))
