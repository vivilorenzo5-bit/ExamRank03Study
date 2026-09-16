def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"

    try:
        decimal_val = int(number, from_base)
    except (ValueError, TypeError):
        return "ERROR"

    if decimal_val == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while decimal_val > 0:
        res = digits[decimal_val % to_base] + res
        decimal_val //= to_base
    return res


if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))   # "10"
    print(number_base_converter("FF", 16, 10))    # "255"
    print(number_base_converter("255", 10, 16))   # "FF"
    print(number_base_converter("123", 10, 2))    # "1111011"
    print(number_base_converter("Z", 36, 10))     # "35"
    print(number_base_converter("35", 10, 36))    # "Z"
    print(number_base_converter("123", 1, 10))    # "ERROR"
    print(number_base_converter("G", 16, 10))     # "ERROR"
