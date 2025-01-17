from classes.Matrix_class import Matrix


def find_determinator() -> float:
    first_parameter = Matrix.matrix_creation()
    return Matrix.find_determinator(matrix=first_parameter)
