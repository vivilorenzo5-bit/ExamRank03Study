def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"

    if not number:
        return "ERROR"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = number.upper()

    decimal_val = 0
    for char in number:
        if char not in digits:
            return "ERROR"
        val = digits.index(char)
        if val >= from_base:
            return "ERROR"
        decimal_val = decimal_val * from_base + val
    if decimal_val == 0:
        return "0"

    res = ""
    while decimal_val > 0:
        remainder = decimal_val % to_base
        res = digits[remainder] + res
        decimal_val //= to_base
    return res
