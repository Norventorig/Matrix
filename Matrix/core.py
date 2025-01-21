from Matrix.utils.matrix_handler import MatrixHandler


matrix_handler = MatrixHandler


def _launch():
    while True:
        while True:
            try:
                answer = int(input("\n1)Сложение матриц"
                                   "\n2)Вычитание матриц"
                                   "\n3)Умножение 2 матриц"
                                   "\n4)Умножение матрицы на число"
                                   "\n5)Решение линейного уравнения"
                                   "\n6)Найти определитель матрицы"
                                   "\nВаш ответ: "))

                if answer > 6 or answer < 1:
                    raise ValueError

            except ValueError:
                print('\nВвод не корректен\n')

            else:
                if answer == 1:
                    matrix_handler.matrix_addition()

                elif answer == 2:
                    matrix_handler.matrix_difference()

                elif answer == 3:
                    matrix_handler.equation()

                elif answer == 4:
                    matrix_handler.matrix_multiplication()

                elif answer == 5:
                    matrix_handler.equation()

                elif answer == 6:
                    matrix_handler.find_determinator()


class UserHandler:
    @staticmethod
    def launch():
        return _launch()
