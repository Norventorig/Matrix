from classes.Matrix_class import Matrix


def matrix_multiplication() -> object:
    first_parameter = Matrix.matrix_creation()
    second_parameter = Matrix.matrix_creation()

    return Matrix.matrix_multiplication(first_object=first_parameter, second_object=second_parameter)
