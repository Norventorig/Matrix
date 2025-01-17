from classes.Matrix_class import Matrix


def matrix_addition() -> object:
    first_parameter = Matrix.matrix_creation()
    second_parameter = Matrix.matrix_creation()

    return Matrix.plus(first_object=first_parameter, second_object=second_parameter)
