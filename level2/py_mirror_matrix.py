def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    result = []
    for row in matrix:
        result.append(row[::-1])
    return result


if __name__ == "__main__":
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(mirror_matrix(m))
    print(mirror_matrix([]))
