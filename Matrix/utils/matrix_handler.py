from Matrix.common.classes import MatrixElem, Matrix


def _matrix_addition() -> object:
    first_parameter = Matrix.matrix_creation()
    second_parameter = Matrix.matrix_creation()

    return Matrix.plus(first_object=first_parameter, second_object=second_parameter)


def _matrix_difference() -> object:
    first_parameter = Matrix.matrix_creation()
    second_parameter = Matrix.matrix_creation()

    return Matrix.minus(first_object=first_parameter, second_object=second_parameter)


def _equation() -> object:
    print('\nСоздание матрицы A:')
    first_object = Matrix.matrix_creation()

    print('\nСоздание матрицы B:')
    second_object = Matrix.matrix_creation()

    return Matrix.equation(first_object=first_object, second_object=second_object)


def _find_determinator() -> float:
    first_parameter = Matrix.matrix_creation()
    return Matrix.find_determinator(matrix=first_parameter)


def _matrix_matrix_multiplication() -> object:
    while True:
        try:
            first_parameter = int(input("\nВведите число на которое будет умножена матрица: "))

        except ValueError:
            print('\nВвод не корректен\n')

        else:
            break

    second_parameter = Matrix.matrix_creation()

    return Matrix.multiplication(first_object=first_parameter, second_object=second_parameter)


def _matrix_multiplication() -> object:
    first_parameter = Matrix.matrix_creation()
    second_parameter = Matrix.matrix_creation()

    return Matrix.matrix_multiplication(first_object=first_parameter, second_object=second_parameter)


class MatrixHandler:
    @staticmethod
    def matrix_addition():
        return _matrix_addition()

    @staticmethod
    def matrix_difference():
        return _matrix_difference()

    @staticmethod
    def equation():
        return _equation()

    @staticmethod
    def find_determinator():
        return _find_determinator()

    @staticmethod
    def matrix_matrix_multiplication():
        return _matrix_matrix_multiplication()

    @staticmethod
    def matrix_multiplication():
        return _matrix_multiplication()
