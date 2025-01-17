from classes.Matrix_class import Matrix


def matrix_matrix_multiplication() -> object:
    while True:
        try:
            first_parameter = int(input("\nВведите число на которое будет умножена матрица: "))

        except ValueError:
            print('\nВвод не корректен\n')

        else:
            break

    second_parameter = Matrix.matrix_creation()

    return Matrix.multiplication(first_object=first_parameter, second_object=second_parameter)
