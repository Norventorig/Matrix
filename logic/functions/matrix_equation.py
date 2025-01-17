from classes.Matrix_class import Matrix


def equation() -> object:
    print('\nСоздание матрицы A:')
    first_object = Matrix.matrix_creation()

    print('\nСоздание матрицы B:')
    second_object = Matrix.matrix_creation()

    return Matrix.equation(first_object=first_object, second_object=second_object)
