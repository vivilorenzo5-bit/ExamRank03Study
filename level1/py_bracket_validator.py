def bracket_validator(s: str) -> bool:
    stack = []
    matching = {
        ')': '(', ']': '[', '}': '{'
    }
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in matching:
            if not stack or stack.pop() != matching[char]:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    print(bracket_validator("([{}])"))
