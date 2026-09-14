def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    for i in range(0, len(list2)):
        list1.append(list2[i])
    return sorted(list1)
