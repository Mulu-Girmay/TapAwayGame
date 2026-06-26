import math


def identity_matrix(size: int = 4) -> list[list[float]]:
    return [
        [1.0 if row == col else 0.0 for col in range(size)]
        for row in range(size)
    ]


def multiply_matrices(left: list[list[float]], right: list[list[float]]) -> list[list[float]]:
    size = len(left)
    result = [[0.0 for _ in range(size)] for _ in range(size)]

    for row in range(size):
        for col in range(size):
            result[row][col] = sum(left[row][k] * right[k][col] for k in range(size))

    return result


def rotation_matrix_x(angle_degrees: float) -> list[list[float]]:
    radians = math.radians(angle_degrees)
    cosine = math.cos(radians)
    sine = math.sin(radians)

    return [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, cosine, -sine, 0.0],
        [0.0, sine, cosine, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def rotation_matrix_y(angle_degrees: float) -> list[list[float]]:
    radians = math.radians(angle_degrees)
    cosine = math.cos(radians)
    sine = math.sin(radians)

    return [
        [cosine, 0.0, sine, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-sine, 0.0, cosine, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def rotation_matrix_z(angle_degrees: float) -> list[list[float]]:
    radians = math.radians(angle_degrees)
    cosine = math.cos(radians)
    sine = math.sin(radians)

    return [
        [cosine, -sine, 0.0, 0.0],
        [sine, cosine, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def flatten_column_major(matrix: list[list[float]]) -> list[float]:
    size = len(matrix)
    values: list[float] = []

    for column in range(size):
        for row in range(size):
            values.append(float(matrix[row][column]))

    return values

