def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []

    n = len(arr)
    k = k % n

    if k == 0:
        return arr.copy()
    return arr[-k:] + arr[:-k]

#    if not arr:
#        return []
#    for _ in range(k):
#        ultimo = arr.pop()
#        arr.insert(0, ultimo)
#    return arr


if __name__ == "__main__":
    print(twist_sequence([1, 2, 3, 4, 5], 2))
    print(twist_sequence([1, 2, 3], 1))
    print(twist_sequence([1, 2, 3, 4], 0))
    print(twist_sequence([1, 2, 3], 5))
    print(twist_sequence([], 3))
